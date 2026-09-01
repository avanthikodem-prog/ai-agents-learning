import os
import time
from dotenv import load_dotenv
from langfuse import Langfuse, observe
import ollama

# 
load_dotenv()

# ------------------------------------------------------
# 
# ------------------------------------------------------
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_BASE_URL")
)


# 
@observe()
def chat_with_tracking(user_message: str):
    start_time = time.time()

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": user_message}]
    )
    reply_text = response["message"]["content"]

    duration = time.time() - start_time
    print(f"(Ollama call took {duration:.2f} seconds)")

    return reply_text


if __name__ == "__main__":
    question = "What is LangGraph?"
    answer = chat_with_tracking(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")

    langfuse.flush()

    print("\nCheck your Langfuse dashboard to see this traced!")