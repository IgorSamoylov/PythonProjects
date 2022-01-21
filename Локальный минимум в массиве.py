

def local_min(a: list) -> int:
    first = 0
    last = len(a) - 1
    
    while first <= last:
        mid = (last - first) // 2
        if a[mid - 1] < a[mid] < a[mid + 1]:
            return mid
        elif a[mid - 1] < a[mid]:
            last = mid - 1
        elif a[mid + 1] < a[mid]:
            first = mid + 1
    return -1

a = [78, 56, 45, 56, 89, 1, 23, 11]
result = local_min(a)
print(result, a[result])
