
#Вызов static - метода без создания экземпляра класса. Нужно в основном только для прямого вызова метода.

class TestClass:
    def __init__(self, n):
        self.testStaticMethod(n)
         
     # Помимо декоратора @staticmethod у static функции отсутствует self в качестве первого аргумента!   
    @staticmethod
    def testStaticMethod(n):
        
        print("ЭТО СТАТИЧЕСКИЙ МЕТОД!", n)
        

TestClass.testStaticMethod('Вызов метода без создания экземпляра класса')

object1 = TestClass('Передача параметра из объекта 1')
object2 = TestClass('Передача параметра из объекта 2')

#ИСПОЛЬЗОВАНИЕ МЕТОДА КЛАССА ДЛЯ СЧЕТЧИКА СОЗДАНИЯ ОБЪЕКТОВ ЭТОГО КЛАССА.
#ТАКЖЕ ПОДДЕРЖИВАЕТ И ПРЯМОЙ ВЫЗОВ, но потребляет больше памяти, чем @staticmethod
class TestClass2:
    invoke_counter = 0 
    def __init__(self, n):
        self.testClassMethod(n)
         
     #  Помимо декоратора @classmethod у метода класса первый аргумент cls! 
    @classmethod
    def testClassMethod(cls, n):
        print("ЭТО МЕТОД КЛАССА!", n, " вызов номер ", cls.invoke_counter)
        cls.invoke_counter += 1
        
TestClass2.testClassMethod('Прямой вызов')
object3 = TestClass2('Вызов метода класса!')
object4 = TestClass2('Вызов метода класса!')


#CLASSMETHOD МОЖНО ПЕРЕДАВАТЬ В КЛАСС-НАСЛЕДНИК
class TestClass3(TestClass2):
    invoke_counter = 0 #Переопределенная переменная в классе-наследника
    pass

object5 = TestClass3
object5.testClassMethod('Вызов из объекта-наследника')
TestClass2.testClassMethod('Прямой вызов')



#STATICMETHOD ТОЖЕ МОЖНО ПЕРЕДАВАТЬ В КЛАСС-НАСЛЕДНИК
class TestClass4(TestClass):
    pass

object6 = TestClass4
object6.testStaticMethod('Вызов из объекта-наследника')





from abc import ABCMeta

class TestClass5(object):
    
    __metaclass__ = ABCMeta
        
    @abstractmethod
    def abstract_method(self):
        pass

