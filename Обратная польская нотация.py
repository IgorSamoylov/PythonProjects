

def rpn(s: str) -> float:
    """Implements Reverse Polish notation (RPN) parsing and calculation with 4 main
    arithmetic binary operations for float numbers"""
    commands = '+-*/'
    stack = Stack()
    number = ''
    for letter in s:
        if letter == ' ':
            if number != '':
                stack.push(number)
                number = ''
            continue
        
        if letter not in commands:
            number += letter
        else:
            y = stack.pop()
            x = stack.pop()
           
            result = str(eval(x + letter + y)) # eval выполняет строку как выражение языка Python
            stack.push(result)
            
    if not stack.is_empty():
        return stack.pop()
    else:
        raise Exception("Not valid expression!")
                        

class Stack:
    """Simple multipurpose stack based on the linked list"""
    class Node:
        def __init__(self, val):
            self.val = val
            self.next_node = None
            
    def __init__(self):
        self.first_node = None
    def push(self, n):
        new_node = Stack.Node(n)
        if self.first_node == None:
            self.first_node = new_node
            return
        new_node.next_node = self.first_node
        self.first_node = new_node
        
    def pop(self):
        if not self.is_empty():
            value = self.first_node.val
            self.first_node = self.first_node.next_node
            return value
        raise Exception('Stack is empty!')
    def is_empty(self):
        return self.first_node == None


print(rpn('7 5 -'))
print(rpn('9000 10 5 + /'))
print(rpn('189.34 454.45 234.23 4534.55 * / +'))

        
