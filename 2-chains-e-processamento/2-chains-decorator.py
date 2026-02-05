from os import getenv

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()


# Define a processing chain that squares a number
@chain
def square(x: int) -> dict:
    return {"square_result": x * x}


question_template = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}.",
)

model = ChatOpenAI(
    api_key=SecretStr(getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1",
    model="stepfun/step-3.5-flash:free",
    temperature=0.5,
)

# Create the chain by composing the processing chain, the prompt template, and the model
chain = square | question_template | model

result = chain.invoke(5)
print(result.content)
