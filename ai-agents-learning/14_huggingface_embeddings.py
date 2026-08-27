from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 1. Create Hugging Face embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Documents
documents = [
    "Python is a programming language.",
    "Python is widely used for machine learning.",
    "FastAPI is a Python framework used for building APIs.",
    "LangChain is used for building applications with language models.",
    "ChromaDB is a vector database used for similarity search."
]

# 3. Store documents + embeddings in ChromaDB
vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=embeddings,
    collection_name="learning_collection"
)

print("Documents stored in ChromaDB.")

# 4. Ask a question
query = input("\nEnter your question: ")

# 5. Similarity search
results = vectorstore.similarity_search_with_score(
    query,
    k=3
)

print("\nMost relevant documents:")

for doc, score in results:
    print(f"Score: {score:.4f}")
    print(f"Document: {doc.page_content}")
    print()