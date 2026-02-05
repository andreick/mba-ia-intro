from os import getenv

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

model = ChatOpenAI(
    api_key=SecretStr(getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3.3-70b-instruct:free",
    temperature=0.5,
)

message = model.invoke("Hello, world!")
print(message.content)
