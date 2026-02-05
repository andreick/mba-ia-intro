from os import getenv

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

question_template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name in it.",
)

model = ChatOpenAI(
    api_key=SecretStr(getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1",
    model="stepfun/step-3.5-flash:free",
    temperature=0.5,
)

# Create the chain by composing the prompt template and the model
chain = question_template | model

result = chain.invoke({"name": "Andreick"})
print(result.content)
