from typing import List
import asyncio
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import uvicorn

app = FastAPI()

class Task(BaseModel):
    id: str
    status: str
    result: List[dict]

tasks = {}

async def process_urls(urls):
    results = []
    for url in urls:
        response_code = await send_request(url)
        results.append({"url": url, "code": response_code})
    return results

async def send_request(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code

@app.post("/api/v1/tasks/", status_code=201)
async def create_task(urls: List[str]):
    task_id = str(uuid.uuid4())
    tasks[task_id] = Task(id=task_id, status="running", result=[])
    asyncio.create_task(process_task(task_id, urls))
    return tasks[task_id]

@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: str):
    if task_id not in tasks:
        return {"error": "Task not found"}
    return tasks[task_id]

async def process_task(task_id, urls):
    results = await process_urls(urls)
    tasks[task_id].status = "ready"
    tasks[task_id].result = results


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
