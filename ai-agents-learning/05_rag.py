from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# 1. Create Ollama model
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 2. Load our knowledge document
# --------------------------------------------------

with open("knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()


# --------------------------------------------------
# 3. Create RAG prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a helpful AI assistant.

        Answer the user's question using ONLY the
        information provided in the context.

        If the answer is not present in the context,
        say: "I don't know based on the provided information."

        Context:
        {context}
        """
    ),
    (
        "human",
        "{question}"
    )
])


# --------------------------------------------------
# 4. Get question from user
# --------------------------------------------------

question = input("Enter your question: ")


# --------------------------------------------------
# 5. Add document + question to prompt
# --------------------------------------------------

messages = prompt.format_messages(
    context=knowledge,
    question=question
)


# --------------------------------------------------
# 6. Ask Ollama
# --------------------------------------------------

response = llm.invoke(messages)


# --------------------------------------------------
# 7. Display answer
# --------------------------------------------------

print("\nAI Response:")
print(response.content)