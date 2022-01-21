

import asyncio

async def async_function(n: int):
    print('Hello!')
    await asyncio.sleep(5)
    print(n)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([async_function(100)]))
