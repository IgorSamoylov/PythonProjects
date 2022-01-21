
def Decorator(function):
    def Obertka():
        print("ФУНКЦИЯ-ОБЕРТКА ДЛЯ:", function)
        function()  #Таким образом запустили переданную как объект функцию
        
    return Obertka


@Decorator
def Base_function():
    print("БАЗОВАЯ ФУНКЦИЯ")

Base_function()



