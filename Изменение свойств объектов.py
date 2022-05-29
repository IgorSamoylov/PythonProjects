

class MyClass:
    def __init__(self):
        self.name = "КОТ БАРСИК"


obj1 = MyClass()

setattr(obj1, 'k', 100)

print(obj1.k)

delattr(obj1, 'name')


val = getattr(obj1, 'k')

attrs = obj1.__dict__

print(attrs)
    
