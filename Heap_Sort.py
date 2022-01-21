

def make_heap(heap):
    for i in range(len(heap)):
        current = i
        parent = (i - 1) // 2
        
        while parent > 0 and heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
            current = parent
            parent = (current - 1) // 2 
            
    return heap

def heap_sort(a):
    result = []
    heap = a[:]
    for i in range(len(a) - 1):
        heap = make_heap(heap)
        result.append(heap.pop())
    return result

import random
result = heap_sort([random.randint(0, 100) for x in range(20)])
print(result)


"""
child1 = i * 2 + 1
child2 = i * 2 + 2
"""
