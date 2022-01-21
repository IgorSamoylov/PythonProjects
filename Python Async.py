import asyncio

async def task(n: int):
    await asyncio.sleep(5) #Специальный sleep для asyncio, не от time!
    print("Асинхронная задача выполнена! ", n)

print("Старт программы!")

futures = [task(100)] # Требует список futures в лупе ожидания

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
