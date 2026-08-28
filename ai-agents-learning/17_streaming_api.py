from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()


def generate_text():
    words = [
        "Hello",
        "this",
        "is",
        "a",
        "streaming",
        "API",
        "using",
        "FastAPI"
    ]

    for word in words:
        yield word + " "
        time.sleep(0.5)


@app.get("/stream")
def stream():
    return StreamingResponse(
        generate_text(),
        media_type="text/plain"
    )