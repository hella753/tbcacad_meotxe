import json
import asyncio
import aiohttp


class AsyncVersion:
    def __init__(self, base_url):
        self.base_url = base_url

    async def main_async(self):
        with open("data_async.json", "w") as start_file:
            json.dump([], start_file)

        await self.fetch_data(78)

    def get_tasks(self, session, idx):
        tasks = []
        for i in range(1, idx):
            tasks.append(asyncio.create_task(session.get(f"{self.base_url}{i}")))
        return tasks

    async def fetch_data(self, idx):
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session, idx)
            responses = await asyncio.gather(*tasks)

            for response in responses:
                data = await response.json()

                with open("data_async.json", "r") as outfile:
                    data_list = json.load(outfile)

                data_list.append(data)

                with open("data_async.json", "w") as outfile:
                    json.dump(data_list, outfile, indent=2)