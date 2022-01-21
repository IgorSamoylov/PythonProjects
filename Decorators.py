
def main ():
    print ('Петух!')
    def pidoras ():
        print ('Пидорас!')
    pidoras()

p = main()

def higher_order(func):
     print(f'Получена функция {func} в качестве аргумента')
     func()
     return func

higher_order(main)


def decorator_function(func):
    def wrapper():  #Обычная функция без аргументов, выполняемая внутри другой ф-ии
        print('Функция-обёртка!')
        print(f'Оборачиваемая функция: {func}')
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

hello_world = decorator_function(hello_world) # то же что и @decorator_function def hello_world():



def benchmark(func):
    import time
    
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')

fetch_webpage()


import requests
import time

def benchmark(func):
    
    
    def wrapper(*args, **kwargs): #Вложенная функция с произвольным кол-вом аргументов
        start = time.time()
        return_value = func(*args, **kwargs)
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
    
    
