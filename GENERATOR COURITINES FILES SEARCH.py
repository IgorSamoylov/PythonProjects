import os
from MyStack import Stack


def folder_traversal(path):
    stack = Stack()
    stack.push(path)

    while not stack.is_empty():
        current_path = stack.pop()
        files_list = os.listdir(current_path)
        if files_list:
            for file_name in files_list:
                current_file = current_path + '/' + file_name
                if os.path.isdir(current_file):
                    stack.push(current_file)
                else:
                    yield current_file


print("Введите путь к директории поиска")
input_path = input()

# Сначала обязательно нужно создать сам объект генератора, поскольку он как "функция" напрямую не работает!
files_generator = folder_traversal(input_path)

n = 0
while True:
    try:
        print(str(n) + "  " + files_generator.__next__())
        n += 1
    except StopIteration:
        break
