

async def ticker(delay, limit):
    for i in range(limit):
        yield i
        await asyncio.sleep(delay)


async def run():
    async for i in ticker(delay=2, limit=10):
        print(i)


import asyncio
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(run())
finally:
    loop.close()
