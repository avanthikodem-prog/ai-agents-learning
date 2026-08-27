from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama


# 1. Create the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 2. Our knowledge base
documents = [
    "Python is a programming language used for machine learning.",
    "FastAPI is a Python framework used for building APIs.",
    "LangChain is a framework for building applications with language models.",
    "ChromaDB is a vector database used for similarity search.",
    "Sentence Transformers are used to convert text into embeddings."
]


# 3. Store documents in ChromaDB
vectorstore = Chroma.from_texts(
    texts=documents,
    embedding=embeddings,
    collection_name="rag_collection"
)

print("Documents stored in ChromaDB.")


# 4. Create the Ollama LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# 5. Ask the user a question
query = input("\nEnter your question: ")


# 6. Retrieve relevant documents
results = vectorstore.similarity_search(query, k=3)

print("\nRetrieved documents:")

for doc in results:
    print("-", doc.page_content)


# 7. Create context from retrieved documents
context = "\n".join(
    doc.page_content for doc in results
)


# 8. Create prompt for the LLM
prompt = f"""
Answer the question using only the information provided in the context.

Context:
{context}

Question:
{query}

Answer:
"""


# 9. Generate final answer
response = llm.invoke(prompt)


# 10. Display answer
print("\nFinal Answer:")
print(response.content)