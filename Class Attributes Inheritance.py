

class Parent1:
    def __init__(self):
        self.n = 100

    #def __init__(self, k):
    #   self.k = k
        
    def action1(self):
        self.n1 = 777
        print('Action 1')

    def action3(self, t):
        print('Action from Parent1')

    

class Parent2:
    def __init__(self):
        self.k = 110
        
    def action2(self):
        self.k1 = 888
        print('Action 2')

    def action3(self):
        print('Action from Parent2')

class Child(Parent2, Parent1):
    pass


ch = Child()
print(ch.k)
ch.action1()
ch.action2()
print(ch.n1, ch.k1)
ch.action3()

    
