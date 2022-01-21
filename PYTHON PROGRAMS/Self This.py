class A:
 a='a'
 def f(this):
  print(this.a) 
a = A()
a.f()

class CLASS1:
 b='b'
 def function1(self):
  print(self.b) 
object1 = CLASS1()
object1.function1()

class Кот:
    def __init__(self, NAME) :                   # Функция __init__ автоматически запускается при создании объекта и принимает аргументы
        print ("Я КОТ ", NAME )
    def мурчало(self) :
        print("мрррр")
    def дай_еды (self) :
        self.мурчало()
        print ("дай еды!")
    def мяв_мяв (self,  gladit) :
        if gladit == True :
            print ("Кот потёрся о спинку")
        else : return print ("Кот ушёл!")
    x = " Громко мяукать "
    y = x * 3

    @staticmethod
    def собака(*arguments) :
        print("ГАВ", arguments)

Кот_Вася = Кот ("ВАСЯ")   # Создание объекта - экземпляра класса Кот с начальным состоянием  ВАСЯ

Кот_Вася.дай_еды()

Кот.дай_еды(Кот_Вася)  # То же самое с передачей объекта в качестве аргумента в метод класса

Кот.мяв_мяв (Кот_Вася, 1) # Объект передаётся как аргумент в метод класса + аргумент для самой функции 

Кот.мяв_мяв (Кот_Вася, 0)

                                                    #Для этого и нужен self - чтобы метод класса знал к какому классу он принадлежит


print (Кот_Вася.y)

Кот_Мурзик = Кот ("МУРЗИК")  # Создание объекта - экземпляра класса Кот с начальным состоянием  МУРЗИК
Кот_Мурзик.дай_еды()

print(Кот.y)       # Инксапсуляция переменных в Питоне не соблюдается!

print(Кот.собака("ЛАЙ!"))  # Обращение к функции - методу класса как к обычной функции, поскольку класс - тоже объект!




def factory(cls):                                                               
    return [cls(), cls(), cls(), cls()]

for x in factory(int): print(x)

for x in factory(float): print(x)


import random
class random_number:                                                            
    def __init__(self):                                                         
        self.var = random.randint(0, 100)                                       
    def __str__(self):                                                          
        return str(self.var)

def factory(cls):                                                               
    return [cls(), cls(), cls(), cls()]

for x in factory(random_number): print(x)





