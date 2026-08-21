from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# Create Ollama model
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI teacher. Explain concepts in simple terms."
    ),
    (
        "human",
        "Explain {topic} in simple terms with one example."
    )
])


# Ask the user for a topic
topic = input("Enter a topic: ")


# Fill the template with the user's topic
messages = prompt.format_messages(topic=topic)


# Send the prompt to Ollama
response = llm.invoke(messages)


# Display the response
print("\nAI Response:")
print(response.content)