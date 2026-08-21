from typing import TypedDict

from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END


# --------------------------------------------------
# 1. Create Ollama model
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 2. Define the state
# --------------------------------------------------

class State(TypedDict):
    question: str
    answer: str


# --------------------------------------------------
# 3. Create a node
# --------------------------------------------------

def ask_llm(state: State):
    response = llm.invoke(state["question"])

    return {
        "answer": response.content
    }


# --------------------------------------------------
# 4. Create the graph
# --------------------------------------------------

graph_builder = StateGraph(State)


# Add our node
graph_builder.add_node("ask_llm", ask_llm)


# Define the flow
graph_builder.add_edge(START, "ask_llm")
graph_builder.add_edge("ask_llm", END)


# --------------------------------------------------
# 5. Compile the graph
# --------------------------------------------------

graph = graph_builder.compile()


# --------------------------------------------------
# 6. Get question from user
# --------------------------------------------------

question = input("Enter your question: ")


# --------------------------------------------------
# 7. Run the graph
# --------------------------------------------------

result = graph.invoke(
    {
        "question": question,
        "answer": ""
    }
)


# --------------------------------------------------
# 8. Display result
# --------------------------------------------------

print("\nAI Response:")
print(result["answer"])