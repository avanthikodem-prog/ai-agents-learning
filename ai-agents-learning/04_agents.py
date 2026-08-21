from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent


# --------------------------------------------------
# 1. Create Ollama model
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 2. Create a calculator tool
# --------------------------------------------------

@tool
def calculator(a: float, b: float, operation: str) -> float:
    """
    Perform a basic mathematical calculation.

    Args:
        a: First number.
        b: Second number.
        operation: add, subtract, multiply, or divide.
    """

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero."

        return a / b

    else:
        return "Unknown operation."


# --------------------------------------------------
# 3. Give the tool to the agent
# --------------------------------------------------

agent = create_agent(
    model=llm,
    tools=[calculator],
    system_prompt="""
    You are a helpful AI assistant.

    Use the calculator tool whenever you need to perform
    mathematical calculations.

    Give accurate answers and explain the result simply.
    """
)


# --------------------------------------------------
# 4. Get question from user
# --------------------------------------------------

question = input("Enter your question: ")


# --------------------------------------------------
# 5. Run the agent
# --------------------------------------------------

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
)


# --------------------------------------------------
# 6. Display the final response
# --------------------------------------------------

print("\nAI Response:")

for message in result["messages"]:
    if message.type == "ai" and message.content:
        print(message.content)