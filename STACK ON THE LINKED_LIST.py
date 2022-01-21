
class Stack:
    
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        self.size = 0
        self.top_node = None
        
    def push(self, inp):
        node = Stack.Node(inp)
        self.size += 1
        if not self.top_node:
            self.top_node = node
            return
        node.next = self.top_node
        self.top_node = node
        
    def pop(self):
        current_top = self.top_node
        self.top_node = self.top_node.next
        self.size -= 1
        return current_top.val

    def size(self):
        return self.size
    def is_empty(self):
        return self.size == 0

    def __iter__(self): 
        return self
    def __next__(self):
        if self.size == 0:
            raise StopIteration
        return self.pop()
    

my_stack = Stack()

for i in range(1, 101):
    my_stack.push(i * 10)

#while not my_stack.is_empty():
#    print(my_stack.pop())

for item in my_stack:
    print(item)



    
while(True):
    i = input()
    if i == "":
        break
    pass
            
        
