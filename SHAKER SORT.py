
def shaker_sort(iList: list[int]) -> list[int]:
    
    left = 0
    right = len(iList) - 1

    while left <= right:
        for i in range(left, right, +1):
            if iList[i] > iList[i + 1]:
                iList[i], iList[i + 1] = iList[i + 1], iList[i]
        right -= 1

        for i in range(right, left, -1):
            if iList[i - 1] > iList[i]:
                iList[i], iList[i - 1] = iList[i - 1], iList[i]
        left += 1
    return iList

def select_sort(iList: list[int]) -> list[int]:
    for i in range(0, len(iList) - 1):
        for k in range(i, len(iList)):
            if iList[i] > iList[k]:
                iList[i], iList[k] = iList[k], iList[i]
    return iList

import random
testList = [random.randint(0, 100) for x in range(100)]
print("TEST LIST: ", testList)

import timeit

result = min(timeit.Timer(lambda : shaker_sort(testList)).repeat(repeat=5, number=1000))
print("SHAKER SORT RESULT ", result)
result = min(timeit.Timer(lambda : select_sort(testList)).repeat(repeat=5, number=1000))
print("SELECT SORT RESULT ", result)

print("SHAKER SORT: ", shaker_sort(testList))
print("SELECT SORT: ", select_sort(testList))
