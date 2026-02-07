from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig, RunnableWithMessageHistory

load_dotenv()

# Prompt and Chain Setup
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chat_model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai", temperature=0.9)

chain = prompt | chat_model

# In-Memory Session Store
session_store: dict[str, InMemoryChatMessageHistory] = {}


# Function to retrieve or create a session history
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


# Wrap the chain with RunnableWithMessageHistory to manage conversation history
conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Configuration for the session
config: RunnableConfig = {"configurable": {"session_id": "demo-session"}}

# Simulate a conversation
response1 = conversational_chain.invoke({"input": "Hello, my name is Andreick. how are you?"}, config=config)
print("Assistant: ", response1.content)
print("-" * 30)

response2 = conversational_chain.invoke({"input": "Can you repeat my name?"}, config=config)
print("Assistant: ", response2.content)
print("-" * 30)

response3 = conversational_chain.invoke({"input": "Can you repeat my name in a motivation phrase?"}, config=config)
print("Assistant: ", response3.content)
print("-" * 30)
