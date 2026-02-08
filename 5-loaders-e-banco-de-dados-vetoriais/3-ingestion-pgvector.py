import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_postgres import PGVector
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

for k in ("PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

current_dir = Path(__file__).parent
pdf_path = current_dir / "gpt5.pdf"

# Load the PDF document
docs = PyPDFLoader(str(pdf_path)).load()

# Split the document into smaller chunks
splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150, add_start_index=False).split_documents(docs)
if not splits:
    raise SystemExit(0)

# Enrich the metadata by removing empty values
enriched = [
    Document(page_content=d.page_content, metadata={k: v for k, v in d.metadata.items() if v not in ("", None)})
    for d in splits
]

# Generate unique IDs for each document
ids = [f"doc-{i}" for i in range(len(enriched))]

# Create embeddings
embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# Create a PGVector store
store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION") or "",
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

# Add documents to the store
store.add_documents(documents=enriched, ids=ids)
