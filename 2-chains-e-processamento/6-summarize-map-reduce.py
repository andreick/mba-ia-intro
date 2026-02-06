from os import getenv

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import SecretStr

load_dotenv()

long_text = """
Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope.
"""

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=70,
)
parts: list[str] = splitter.split_text(long_text)

for part in parts:
    print(part)
    print("-" * 30)

# LLM and parser
llm = ChatOpenAI(
    api_key=SecretStr(getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1",
    model="stepfun/step-3.5-flash:free",
    temperature=0,
)
parser = StrOutputParser()

# MAP: summarize each chunk
map_prompt = ChatPromptTemplate.from_template("Write a concise summary of the following:\n\n{chunk}")
map_chain = map_prompt | llm | parser

# REDUCE: combine all summaries
reduce_prompt = ChatPromptTemplate.from_template(
    "Combine the following summaries into a single concise summary:\n\n{summaries}"
)
reduce_chain = reduce_prompt | llm | parser


# Runnable to build inputs: list[str] -> list[dict[str, str]]
def to_inputs_fn(chunks: list[str]) -> list[dict[str, str]]:
    return [{"chunk": d} for d in chunks]


to_inputs = RunnableLambda(to_inputs_fn)


# Runnable to join summaries: list[str] -> str
def join_summaries_fn(summaries: list[str]) -> str:
    return "\n\n".join(summaries)


join_summaries = RunnableLambda(join_summaries_fn)

# Pipeline: PARTS -> TO_INPUTS -> MAP (per-chunk) -> JOIN -> REDUCE
pipeline = to_inputs | map_chain.map() | join_summaries | reduce_chain

result = pipeline.invoke(parts)
print(result)

# Optional: streaming
# for token in pipeline.stream(parts):
#     print(token, end="", flush=True)
