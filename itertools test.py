import itertools as itt

list1 = [x for x in range(5)]
list2 = [x for x in range(100, 105)]

result_list = [x for x in itt.product(list1, list2)]
print(f"itertools product:\n {result_list}")

group = 3
result_list = [x for x in itt.combinations(list1, group)]
print(f"itertools combinations:\n {result_list}")

result_list = [x for x in itt.permutations(list1, group)]
print(f"itertools permutations:\n {result_list}")

result_list = [x for x in itt.chain(list1, list2)]
print(f"itertools chain:\n {result_list}")

result_list = [0] * 20
itt_cycle = itt.cycle(list1)
for count in range(20):
    result_list[count] = next(itt_cycle)
print(f"itertools cycle:\n {result_list}")

"""Создаёт несколько итераторов для одного итерируемого объекта.
    itertools.tee(iterable, n=2) -> tuple(iterator, iterator) """
iterators_tuple3 = itt.tee(list1, 3)
for iterator in iterators_tuple3:
    result_list = [x for x in iterator]
    print(f"itertools tee:\n {result_list}")


def grouper(x: int) -> int:
    if x == 0:
        return 0
    elif x < 3:
        return 1
    else:
        return 2
"""Создает объект itertools.groupby, являющийся итератором по кортежам,
содержащим ключ группировки первым элементом и объект группировки,
представляющий собой итератор по всем элементам исходного iterable,
соответвующим этому ключу"""    
iterator_group_obj = itt.groupby(list1, grouper)
for key, tup in iterator_group_obj:
    result_list = [*tup]
    print(f"itertools group by key: {key} elements: {result_list}")
