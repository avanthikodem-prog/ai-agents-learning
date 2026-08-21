from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


question = input("Enter your question: ")

response = llm.invoke(question)

print("\nAI Response:")
print(response.content)