
def inverse_list(N: list):
    """ Обращение массива задом наперёд """
    # Идем до целочисленной половины, независимо от количества (операция с элементом
    # в центре при нечетном количестве элементов в списке просто не будет выполняться)
    for i in range(len(N) // 2):  
        N[i], N[len(N) - 1 - i] = N[len(N) - 1 - i], N[i]

# Автоматическое тестирование
def test_inverse_list():
    N = [x for x in range(5)]
    print(N)
    inverse_list(N)
    print(N)
    if N == [x for x in range(4, -1, -1)]:
        print('#test1 - ok')
    else:
        print('#test1 - fail')

    N2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(N2)
    inverse_list(N2)
    print(N2)
    if N2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('#test2 - ok')
    else:
        print('#test2 - fail')

test_inverse_list()
