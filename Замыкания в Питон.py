

def test():
    x = 1
    y = 2
    z = "test"
    def test2():
        nonlocal x, y, z
        x += 1
    return test2

a = test()
print(a.__closure__)  #Получение атрибута __closure__ для функции
print(a.__closure__[2].cell_contents) # Получение содержимого 3-го cell closure
a.__closure__[2].cell_contents = "CAT" # Содержимое контейнера контекста замыкания можно изменять
print(a.__closure__[2].cell_contents)



def func_as_object(a, b):
    def add():
        return a + b
    def sub():
        return a - b
    def mul():
        return a * b
    func_as_object.add = add
    func_as_object.sub = sub
    func_as_object.mul = mul
    return func_as_object

a = func_as_object(1, 3) # Создаем объект внешней функции и запоминаем параметры
print(a.add () ) # Так вызываем нужную функцию с исходными параметрами, сам метод не принимает никакие аргуметы 
print(a.sub () )
print(a.mul () )


# Более наглядная замена рекурсивной функции посредством вызова вложенной функции из начального контекста
def func1():
    a = 1
    b = 'line'
    c = [1, 2, 3]

    def func2():
        nonlocal a
        c.append(4)
        a += 1
        return a, b, c
    return func2

a = func1()

for i in range(20):
    print(a())

