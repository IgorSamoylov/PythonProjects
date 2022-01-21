

def Decorator(inputFunction):
    def InnerFunction():      #Внутренняя функция имеет доступ к переменным внешней
        print("Обёртываю эту функцию!")
        inputFunction()

    return InnerFunction


@Decorator
def Main():
    print("I AM COOL!")

Main()
