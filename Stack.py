class Stack:
    """Простейшая имплементация стека с использованием list"""
    def __init__(self):
        self.container = []
        
    def push(self, x):
        #print('Push', x)
        self.container.append(x)
        
    def pop(self):
        #print('Pop', self.container[-1])
        return self.container.pop()

    def top(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.container.clear()
