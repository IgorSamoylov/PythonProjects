from collections.abc import Iterable
 
def wrap_class(cls): #В функцию рефлексивно передаётся тип обобщённого класса - cls
    if issubclass(cls, Iterable): #Если cls является подклассом Iterable
        class FooCounter(cls): #Создаётся новый класс, наследник cls
             def count_foo(self): #В котором определена функция
                 return sum(1 for item in self if item == 'foo')
                #Генераторное выражение с условием внутри функции суммирования
 
        return FooCounter
    #Если if не выполнен, выкинуть исключение
    raise TypeError(f'Class {cls} is not an iterable type')
 
print(wrap_class(list)([2, 3, 'foo', 'bar', 'baz', 'foo']).count_foo())

print(wrap_class(tuple)(('foo', 'foo', 'foo', 'foo')).count_foo())

print(wrap_class(set)({'foo', 'foo', 'foo', 'foo','foo','bar','bar'}).count_foo())


