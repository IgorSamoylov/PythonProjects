

def wrapper(number):
    
    def test1(function):
        return function() + 'World! ' + str(number)
    
    return test1  #Возвращаем подменную функцию как объект в исходное место, не вызываем ее!

# Декоратор вызывает функцию wrapper, передает туда нашу функцию test как объект
# в виде аргумента, а возвращает функцию-объект, возращенную wrapper
@wrapper(10)  
def test():
    return 'Hello '

print(test) # ???Здесь происходит вызов
