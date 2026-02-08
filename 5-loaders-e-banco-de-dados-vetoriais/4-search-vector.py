import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_postgres import PGVector

load_dotenv()

for k in ("PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

query = "Tell me more about the gpt-5 thinking evaluation and performance results comparing to gpt-4"

embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION") or "",
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

# Perform a similarity search with the query and retrieve the top 3 results
results = store.similarity_search_with_score(query, k=3)

for i, (doc, score) in enumerate(results, start=1):
    print("=" * 50)
    print(f"Resultado {i} (score: {score:.2f}):")
    print("=" * 50)

    print("\nTexto:\n")
    print(doc.page_content.strip())

    print("\nMetadados:\n")
    for k, v in doc.metadata.items():
        print(f"{k}: {v}")
