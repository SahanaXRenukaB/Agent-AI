# FastAPI backend to take user questions and return answers from database

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, StreamingResponse
from query_handler import handle_question

app = FastAPI()

@app.get("/ask")
def ask(question: str = Query(..., description="Ask a question about your ecommerce data")):
    result = handle_question(question)
    return JSONResponse(content=result)

@app.get("/stream")
def stream(question: str):
    def stream_gen():
        result = handle_question(question)
        yield f"data: {result}\n\n"

    return StreamingResponse(stream_gen(), media_type="text/event-stream")
