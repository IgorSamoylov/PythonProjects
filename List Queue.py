
#import timeit
#test = '''

class ListQueue:
    def __init__(self):
        self.list = []

    def push_back(self, val):
        self.list.append(val)

    def pop_front(self):
        return self.list.pop(0)

queue = ListQueue()
for i in range(100):
    queue.push_back(i)

for i in range(100):
    print(queue.pop_front(), end=' ')
    #queue.pop_front()
#'''
#print(min(timeit.Timer(setup=test).repeat(100)))
