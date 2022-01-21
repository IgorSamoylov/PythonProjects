

class TestClass:
    def test():
        self.n = 100

testClass = TestClass()
testClass.attr = 12
print(testClass.__dict__)
print(TestClass.__dict__)

def f(): pass
print(f.__class__)


#Для удобства получения интроспективной информации в Python есть модуль inspect[91].

import inspect
def f(x,y = 10,**mp):pass

print(inspect.getfullargspec(f))
 
 
# С помощью модуля new возможен обратный процесс — построения объекта из составных частей на этапе исполнения

def f(i): return j + i

j = 2
print(f(1))

import new_
g = new.function(f.func_code, {'j': 23})
print(g(1))


i = int(input())

input("prompt: ")
