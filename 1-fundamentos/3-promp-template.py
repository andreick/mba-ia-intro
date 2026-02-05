from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}! Tell me a joke with my name in it.",
)

text = template.format(name="Andreick")
print(text)
