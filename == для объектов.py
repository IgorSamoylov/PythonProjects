# По умолчанию на == для объектов идёт ссылочное сравнение (как это срабатывает и в JAVA)
class Test0:
    def __init__(self, n):
        self.n = n

test_obj1 = Test0(10)
test_obj2 = Test0(10)
test_obj3 = test_obj1

print(test_obj1 == test_obj2)
print(test_obj3 == test_obj1)


class Test:
    def __init__(self, n):
        self.n = n

    # Перегружаем оператор == для обеспечения сравнения объектов
    def __eq__(self, obj2):
        if isinstance(obj2, Test):
            return self.n == obj2.n
        return False

test_obj1 = Test(10)
test_obj2 = Test(10)
print(test_obj1 == test_obj2)

test_obj3 = Test(7)
print(test_obj1 == test_obj3)
