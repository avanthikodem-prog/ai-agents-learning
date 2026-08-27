import chromadb
from langchain_ollama import ChatOllama

# -----------------------------
# 1. Create ChromaDB client
# -----------------------------

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="rag_documents"
)


# -----------------------------
# 2. Add documents
# -----------------------------

documents = [
    "Python is a popular programming language used for machine learning.",
    "Machine learning uses algorithms to learn patterns from data.",
    "FastAPI is a Python framework used for building APIs.",
    "LangChain is a framework for building applications powered by language models."
]

collection.add(
    documents=documents,
    ids=["1", "2", "3", "4"]
)

print("Documents stored in ChromaDB.")


# -----------------------------
# 3. Ask a question
# -----------------------------

question = input("\nEnter your question: ")


# -----------------------------
# 4. Retrieve relevant documents
# -----------------------------

results = collection.query(
    query_texts=[question],
    n_results=2
)

retrieved_documents = results["documents"][0]

print("\nRetrieved documents:")

for document in retrieved_documents:
    print("-", document)


# -----------------------------
# 5. Create context
# -----------------------------

context = "\n".join(retrieved_documents)


# -----------------------------
# 6. Create prompt
# -----------------------------

prompt = f"""
Answer the question using only the information provided below.

Context:
{context}

Question:
{question}

Answer:
"""


# -----------------------------
# 7. Send to Ollama
# -----------------------------

llm = ChatOllama(
    model="llama3.2"
)

response = llm.invoke(prompt)


# -----------------------------
# 8. Print final answer
# -----------------------------

print("\nFinal Answer:")
print(response.content)