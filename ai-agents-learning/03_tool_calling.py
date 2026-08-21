from langchain_ollama import ChatOllama
from langchain_core.tools import tool


# Create Ollama model
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# Create a calculator tool
@tool
def calculator(a: float, b: float, operation: str) -> float:
    """
    Perform a basic mathematical calculation.

    Args:
        a: First number.
        b: Second number.
        operation: One of add, subtract, multiply, or divide.
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


# Give the tool to the model
llm_with_tools = llm.bind_tools([calculator])


# Get question from user
question = input("Enter your question: ")


# Ask the model
response = llm_with_tools.invoke(question)


# Check whether the model wants to call a tool
if response.tool_calls:
    print("\nTool Call:")
    print(response.tool_calls)

else:
    print("\nAI Response:")
    print(response.content)