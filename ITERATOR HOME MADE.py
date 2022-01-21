class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

# Если мы хотим, чтобы с данным объектом можно было работать в цикле for,
# то в класс SimpleIterator нужно добавить метод __iter__(), который возвращает итератор,
# в данном случае этот метод должен возвращать self.

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration
        
s_iter1 = SimpleIterator(3)
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
