from abc import ABCMeta, abstractmethod

class MyClass(metaclass = ABCMeta):
    
    def __init__(self, n):
        self.n = n
        
    @abstractmethod
    def getN(self):
        return self.n

mc = MyClass(100)
print(mc.getN())

	
