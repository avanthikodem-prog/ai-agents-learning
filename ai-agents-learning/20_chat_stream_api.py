import os
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import json
from dotenv import load_dotenv
from langfuse import Langfuse, observe

load_dotenv()

app = FastAPI()

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_BASE_URL")
)


class ChatRequest(BaseModel):
    prompt: str


@observe(name="chat-stream-request")
def ollama_stream(prompt: str):
    url = "http://localhost:11434/api/chat"
    data = {
        "model": "llama3.2",
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }

    start_time = time.time()
    full_response = ""

    response = requests.post(url, json=data, stream=True)
    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            result = json.loads(line)
            content = result.get("message", {}).get("content", "")
            if content:
                full_response += content
                yield f"data: {content}\n\n"

    duration = time.time() - start_time

    langfuse.update_current_span(
        input={"prompt": prompt},
        output=full_response,
        metadata={"duration_seconds": round(duration, 2)}
    )

    langfuse.flush()


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    return StreamingResponse(
        ollama_stream(request.prompt),
        media_type="text/event-stream"
    )