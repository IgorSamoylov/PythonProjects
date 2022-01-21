#import timeit
#test = '''

class MyQueue:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next_node = None

    def __init__(self):
        self.first_node = None
        self.last_node = None

    def push_back(self, val):
        new_node = MyQueue.Node(val) # По умолчанию Питон не видит вложенные классы, нужно указать "путь" к ним через внешний!
        if self.last_node == None:
            self.first_node = self.last_node = new_node
            return
        self.last_node.next_node = new_node
        self.last_node = new_node

    def pop_front(self):
        if self.first_node: 
            val = self.first_node.val
            self.first_node = self.first_node.next_node
            return val


queue = MyQueue()
for i in range(100):
    queue.push_back(i)

for i in range(100):
    print(queue.pop_front())
    #queue.pop_front()
    
#'''
#print(min(timeit.Timer(setup=test).repeat(100)))
