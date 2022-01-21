import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
        
    def __iter__(self):
        while self.i < self.k:
            self.i += 1
            yield random.random() # yield в объекте-генераторе вызывается методом __next__

   


random_iter = RandomIterator(10)
for i in random_iter:
    print(i)
