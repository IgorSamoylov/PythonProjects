

class Node:
    # Объявляем общие переменные класса, хранящие ссылку на первый Node и на итерируемый 
    first_node = None
    iter_node = None
    
    def __init__(self):     
        self.val = None # Инициализируем переменные экземпляра - объекта
        self.next = None
        
        if not Node.first_node: # Устанавливаем переменные класса на первый Node
            Node.first_node = self # Обращение к переменным класса идет по имени класса через .
            

    # Функция __iter__ должна возвращать объект-итератор, в данном случае им
    # будет само первое ядро    
    def __iter__(self):
        Node.iter_node = Node.first_node # Устанавливаем IterNode на начало 
        return Node.first_node
    
    # Затем цикл for будет вызывать у объекта - итератора метод __next__ до тех пор,
    # пока не выкинет исключение StopIteration
    def __next__(self):
        current_node = Node.iter_node # Запоминаем текущий Node для возврата его как результата
        Node.iter_node = Node.iter_node.next # Итерируем переменную класса на следующий Node
        if not Node.iter_node:
            raise StopIteration
        return current_node
    


node = Node()
#first_node = node
for i in range(100):
    node.val = i
    next_node = Node()
    node.next = next_node
    print(node.val, "  ", node.next)
    node = next_node

# Теперь наш LinkedList доступен в обычном цикле Питон через обращение к любому node
for n in node:
    print(n.val)
