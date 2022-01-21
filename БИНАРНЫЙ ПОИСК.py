
def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

A = [1, 3, 3, 5, 5, 7, 7, 10]
print(left_bound(A, 6))
print(right_bound(A, 6))
