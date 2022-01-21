def merge_sort(data):
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        #print(data)
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


List1 = [1, 4, 777, 555, 34, 0 , 23, 98, 11, 2, 3, 24, 55]
print(merge_sort(List1))

import random

List2 = [random.random() for x in range (0, 1000)]
print(merge_sort(List2))
