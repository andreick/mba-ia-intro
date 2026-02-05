from os import getenv

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

system = ("system", "You are an assistant that answers questions in a {style} style.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate.from_messages([system, user])

messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

for message in messages:
    print(f"{message.type}: {message.content}")

model = ChatOpenAI(
    api_key=SecretStr(getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3.3-70b-instruct:free",
    temperature=0.5,
)

result = model.invoke(messages)
print(result.content)
