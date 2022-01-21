class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
        print(item)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        return self.list == []