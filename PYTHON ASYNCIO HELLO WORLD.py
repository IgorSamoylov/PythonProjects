import asyncio

async def test():
    print("Добро пожаловать...")
    await asyncio.sleep(10)
    print("... в асинхронный мир!")

print("first step")
asyncio.run(test())
print("next step")
