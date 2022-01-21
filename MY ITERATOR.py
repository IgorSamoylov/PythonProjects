
class MyIterator:
    
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.i = -1
        
    def __iter__(self):  #Для использования в цикле for нужно определить функцию __iter__, возвращающую сам объект итератора
        return self

    def __next__(self):  #Цикл for просто вызывает метод __next__
        self.i += 1
        return self.iter_obj[self.i]
        
        
data = [1,2,3,5,6,7]
my_Iterator = MyIterator(data)
#while(True):
 #   print(next(my_Iterator))

try:
    for i in my_Iterator:
        print(i)
except:
    pass
    #print("End of iterable")


data = ("К","О","Т"," ","Д","О","Б","Р","Ы","Й")
my_Iterator2 = MyIterator(data)

try:
    for i in my_Iterator2:
        print(i)
except:
    pass

