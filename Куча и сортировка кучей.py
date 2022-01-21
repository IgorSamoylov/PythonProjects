import random


class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, inp):
        self.values.append(inp)
        self.size += 1
        self._sift_up(self.size - 1)

    def _sift_up(self, item_n):
        parent = (item_n - 1) // 2
        while item_n != 0 and self.values[item_n] < self.values[parent]:
            self.values[item_n], self.values[parent] = self.values[parent], self.values[item_n]
            item_n = parent
            parent = (item_n - 1) // 2 # Parent вычисляется по одной формуле для левого и правого потомка

    def extract_min(self):
        assert self.size > 0, "Heap is empty"
        result = self.values[0]
        self.values[0], self.values[-1] = self.values[-1], self.values[0]
        self.values.pop()
        self.size -= 1
        self.sift_down3(0)
        return result

    # Неправильная версия из лекции
    def _sift_down(self, i):
        left_child_iter = 2 * i + 1
        while left_child_iter < self.size:  # Пока есть хотя бы левый потомок
            big_val_iter = i
            if self.values[left_child_iter] < self.values[i]:
                big_val_iter = left_child_iter
            right_child_iter = 2 * i + 2
            if right_child_iter < self.size and self.values[right_child_iter] < self.values[
                big_val_iter]:  # Если есть второй потомок
                big_val_iter = right_child_iter
            if i == big_val_iter:
                break
            self.values[i], self.values[big_val_iter] = self.values[big_val_iter], self.values[i]

    def _sift_down2(self, i):
        left_child_it = 2 * i + 1
        right_child_it = 2 * i + 2
        while left_child_it < self.size:
            big_it = i
            if self.values[i] > self.values[left_child_it]:
                big_it = left_child_it
            if right_child_it < self.size and self.values[big_it] > self.values[right_child_it]:
                big_it = right_child_it
            if big_it == i:
                break
            self.values[i], self.values[big_it] = self.values[big_it], self.values[i]
            i = big_it
            left_child_it = 2 * i + 1
            right_child_it = 2 * i + 2

    def sift_down3(self, i):
        """
        Принимает на вход индекс элемента в списке self.values
        и перемещает его вниз, сохраняя свойства кучи
        """
        
        while 2 * i + 1 < self.size:
            left = 2 * i + 1
            right = 2 * i + 2
            big = left
            if right < self.size and self.values[right] < self.values[left]:
                big = right
            if self.values[i] <= self.values[big]:
                break
            self.values[i], self.values[big] = self.values[big], self.values[i]
            i = big


def heap_sort(arr):
    heap = Heap()
    for item in arr:
        heap.insert(item)

    sorted_arr = []
    while heap.size:
        sorted_arr.append(heap.extract_min())

    return sorted_arr

def heap_sort_fast(arr):
    """
    Оптимизирует время создания кучи до O(N) вместо O(N * log(N)) за счет
    прохода только тех вершин, которые имеют хотя бы одного потомка,
    а следовательно находятся в области floor(N/2) в массиве значений кучи
    """
    heap = Heap()
    heap.values = arr[:]
    heap.size = len(arr)
    for i in reversed(range(heap.size // 2)): # Идём с конца области N/2
        heap.sift_down3(i)

    sorted_arr = []
    while heap.size:
        sorted_arr.append(heap.extract_min())

    return sorted_arr

HEAP_SIZE = 100
unsorted_list = [random.randint(0, 1000) for i in range(100)]
sorted_list = heap_sort_fast(unsorted_list)
print(sorted_list)


