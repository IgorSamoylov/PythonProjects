# Implements simple binary search algorithm

test_list = [x for x in range(1, 100)]
print(test_list)


def binary_search(x: list[int], target: int) -> int:
    if x is None or target is None:
        raise Exception("Empty input data!")
    
    # Boundary values ​​are not available for this algorithm
    if x[0] == target:
        return 0
    if x[len(x) - 1] == target:
        return len(x) - 1

    # Divide with rounding by mathematical rules for find center of the list
    i = int(len(x) / 2 + 0.5)
    mid = i

    # Main algorithm
    while x[i] != target:
        if mid > 1:
            mid = int(mid / 2 + 0.5)
        else:
            return None

        if target < x[i]:
            i -= mid
        else:
            i += mid

        print("testing index: ", i, " divider:  ", mid)

        if i > len(x) - 1 or i < 0:
            raise Exception("Index not found")

    return i 


n = 77
print(f"Found {n} in list at index: ", binary_search(test_list, n))
