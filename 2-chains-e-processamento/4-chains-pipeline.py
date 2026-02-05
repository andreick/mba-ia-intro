from os import getenv

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English:\n ```{initial_text}```",
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```",
)

llm = ChatOpenAI(
    api_key=SecretStr(getenv("OPENROUTER_API_KEY") or ""),
    base_url="https://openrouter.ai/api/v1",
    model="stepfun/step-3.5-flash:free",
    temperature=0,
)

# Create the pipeline by composing the translation and summary chains
translate = template_translate | llm | StrOutputParser()  # Result of translation is plain text
summary = template_summary | llm | StrOutputParser()  # Result of summary is plain text

pipeline = {"text": translate} | summary

result = pipeline.invoke({"initial_text": "LangChain é um framework para desenvolvimento de aplicações de IA."})
print(result)
