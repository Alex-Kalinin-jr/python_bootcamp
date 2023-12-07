from typing import List
import asyncio
import uuid
from fakeredis import aioredis
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from uvicorn import Config, Server
import www_help


redis = aioredis.FakeRedis()
app = FastAPI()
#*********************************************************************************

class Task(BaseModel):
    id: str
    status: str
    result: List[dict]

tasks = {}

#******************************REDIS_RELATED**************************************

async def process_urls(urls):
    results = []
    for url in urls:
        www = www_help.extract_domain(url)
        await redis.incr(www)
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

@app.get("/api/v1/redis")
async def get_redis():
    redis_data = {}
    keys = await redis.keys()
    for key in keys:
        redis_data[key] = await redis.get(key)
    return redis_data

async def process_task(task_id, urls):
    results = await process_urls(urls)
    tasks[task_id].status = "ready"
    tasks[task_id].result = results


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    config = Config(app=app, loop=loop, host="0.0.0.0", port=8888)
    server = Server(config)
    server_task = loop.create_task(server.serve())
    loop.run_until_complete(server_task)
