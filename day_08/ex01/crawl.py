import asyncio
import httpx

URL = "http://localhost:8888/"


async def submit_urls(urls):
    async with httpx.AsyncClient() as client:
        response = await client.post(URL + 'api/v1/tasks/', json=urls)
        if response.status_code == 201:
            task_id = response.json()['id']
            return task_id
        return None

async def check_task_status(task_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(URL + f'api/v1/tasks/{task_id}')
        if response.status_code == 200:
            task_status = response.json()['status']
            return task_status
        return None

async def print_task_results(task_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(URL + f'api/v1/tasks/{task_id}')
        if response.status_code == 200:
            task_result = response.json()['result']
            for result in task_result:
                print(f"{result['code']}\t{result['url']}")
        else:
            return None

async def print_redis_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL + 'api/v1/redis')
        if response.status_code == 200:
            redis_data = response.json()
            for key, value in redis_data.items():
                print(f"{key}\t{value}")

async def main(urls: list):
    task_id = await submit_urls(urls)
    task_status = 'running'
    while task_status != 'ready':
        task_status = await check_task_status(task_id)
    await print_task_results(task_id)
    await print_redis_data()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('urls', nargs='+', type=str)
    args = parser.parse_args()
    urls = args.urls
    asyncio.run(main(urls))
