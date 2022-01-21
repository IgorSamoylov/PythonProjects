
import random

class Sequence:
    def __init__(self):
        self.inner_list = [random.randint(0, 100) for x in range(20)]
        
    def __iter__(self):
        
        class SequenceIterator:
            def __init__(self, outer_instance):
                self.outer_instance = outer_instance
                self.index = -1
            def __next__(self):
                self.index += 1
                if self.index == len(self.outer_instance.inner_list):
                    raise StopIteration # Просто StopIteration
                return self.outer_instance.inner_list[self.index]
            
        return SequenceIterator(self) # Вынуждены передавать инстанс внешнего класса во внутренний
                
sequence = Sequence()
for x in sequence:
    print(x)



