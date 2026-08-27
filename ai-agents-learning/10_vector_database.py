import chromadb

# Create ChromaDB client
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="documents")

# Add documents
documents = [
    "Python is a popular programming language.",
    "Machine learning uses algorithms to learn from data.",
    "Cricket is a popular sport in India.",
    "FastAPI is a Python framework for building APIs."
]

collection.add(
    documents=documents,
    ids=["1", "2", "3", "4"]
)

print("Documents stored successfully!")

# Search
query = input("\nEnter your question: ")

results = collection.query(
    query_texts=[query],
    n_results=2
)

print("\nMost relevant documents:")

for document in results["documents"][0]:
    print("-", document)