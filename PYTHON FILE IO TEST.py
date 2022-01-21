import asyncio


file_path = "C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/ПРОГРАММИРОВАНИЕ НА PYTHON.txt"
       

def read_file(file_name):
    f = open(file_name)
    f.seek(90000)
    return f.read()

async def main():
    in_loop = asyncio.get_event_loop()
    data = await in_loop.run_in_executor(None, read_file, file_path)
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())       




