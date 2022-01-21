import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print(f'Starting {url}')
    async with aiohttp.ClientSession() as session:
        
        async with session.get(url) as response:
            
            print(response.status)
            
            data = await response.text()
            
            print(url, " ", len(data), " bytes: ", data)
    return data

futures = [call_url(url) for url in urls]

# Получаем луп ожидания
loop = asyncio.get_event_loop()

# Запускаем луп до завершения наполнения листа futures
loop.run_until_complete(asyncio.wait(futures))
