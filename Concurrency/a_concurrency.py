import aiohttp
import asyncio
import json
import time

INPUT_FILE = 'values.json'
ADDRESS = 'http://localhost:8080/'

values = []
output = {}
data = []
with open(INPUT_FILE) as f:
    values = json.load(f)

start_time = time.time()

async def main():
    async with aiohttp.ClientSession() as session:
        for start, end in values:
            url = ADDRESS + '?start=%s&end=%s' % (start, end)
            async with session.get(url) as resp:
                r = await resp.json()
                data.append(r)

asyncio.run(main())

output['time'] = time.time() - start_time
output['name'] = 'asynchronous'
output['data'] = data


with open("output.json", "r") as f:
    if f.read():
        with open("output.json", "r") as f:
            data = json.load(f)
        data.append(output)
        with open("output.json", "w") as f:
            json.dump(data, f)
    else:
        with open("output.json", "w") as f:
            json.dump([output], f)