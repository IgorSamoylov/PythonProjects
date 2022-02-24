

class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    
    def __setName(self, n):
        self.__name = n

    def __getName(self):
        return self.__name

    name=property(__getName, __setName)
    #age=property(__getAge)
    
    @property
    @age.getter
    def __getAge(self):
        return self.__age

    
    

cat1 = Cat('Barsik', 10)
cat1.name = 'Bars'
print('{o.name} {o.age}'.format(cat1))

