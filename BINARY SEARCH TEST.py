# Implements simple binary search algorithm

test_list = [x for x in range(1, 100)]
print(test_list)


def binary_search(x: list[int], target: int) -> int:
    if x is None or target is None:
        raise Exception("Empty input data!")

    i = len(x) // 2
    mid = i

    while x[i] != target:
        if mid > 1:
            if mid % 2 == 1:
                mid = mid // 2 + 1
            else:
                mid //= 2
        else:
            break

        if target < x[i]:
            i -= mid
        else:
            i += mid

        print("testing index: ", i, " divider:  ", mid)

        if i > len(x) - 1 or i < 0:
            raise Exception("Index not found")

    return i if x[i] == target else None


n = 10
print(f"Found {n} in list at index: ", binary_search(test_list, n))
