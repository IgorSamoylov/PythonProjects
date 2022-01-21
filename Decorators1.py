import requests
import time

def benchmark(func):
    
    
    def wrapper(*arg): #Вложенная функция с произвольным кол-вом аргументов
        start = time.time()
        return_value = func(*arg)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))
        return return_value
    return wrapper



@benchmark
def fetch_webpage(url):   
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)
