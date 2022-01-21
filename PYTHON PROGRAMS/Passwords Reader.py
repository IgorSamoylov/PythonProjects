

class PasswordReader:
    
    def __init__(self):
        F = open('10000passwords.txt', 'r')
        passwords_data = F.read()
        F.close
        self.passwords = passwords_data.split("\n")
        self.i = -1 #Эта переменная, будучи определена в конструкторе, является
        #собственной переменной объекта

    def get_next(self):
        self.i += 1
        return self.passwords[self.i]

    k = -1 #Эта переменная единая для всех объектов!
    def get_next2(self):   
        PasswordReader.k += 1 #Вот как можно получить доступ к переменной класса!
        return self.passwords[self.k]

    
      

passwordReader = PasswordReader()

for i in range(10):
    print(passwordReader.get_next())

for i in range(10):
    print(passwordReader.get_next2())

passwordReader2 = PasswordReader()

for i in range(10):
    print(passwordReader2.get_next2())
    
        
        
