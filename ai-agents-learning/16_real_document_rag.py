from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama


# --------------------------------------------------
# 1. Load the document
# --------------------------------------------------

loader = TextLoader("documents/python.txt", encoding="utf-8")

documents = loader.load()

print("Document loaded successfully.")
print("Number of documents:", len(documents))


# --------------------------------------------------
# 2. Split document into smaller chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Number of chunks:", len(chunks))


# --------------------------------------------------
# 3. Create Hugging Face embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 4. Store chunks and embeddings in ChromaDB
# --------------------------------------------------

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="python_documents"
)

print("Documents stored in ChromaDB.")


# --------------------------------------------------
# 5. Create Ollama LLM
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 6. Ask user a question
# --------------------------------------------------

query = input("\nEnter your question: ")


# --------------------------------------------------
# 7. Retrieve relevant chunks
# --------------------------------------------------

results = vectorstore.similarity_search(
    query,
    k=3
)

print("\nRetrieved chunks:")

for i, doc in enumerate(results, start=1):
    print(f"\nChunk {i}:")
    print(doc.page_content)


# --------------------------------------------------
# 8. Create context
# --------------------------------------------------

context = "\n\n".join(
    doc.page_content
    for doc in results
)


# --------------------------------------------------
# 9. Create RAG prompt
# --------------------------------------------------

prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the information provided
in the context below.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{query}

Answer:
"""


# --------------------------------------------------
# 10. Generate final answer
# --------------------------------------------------

response = llm.invoke(prompt)


# --------------------------------------------------
# 11. Display final answer
# --------------------------------------------------

print("\nFinal Answer:")
print(response.content)