

x = 111

def inner():
    x = 10

    code_str = 'print(1 + x + 1000)'

    exec(code_str, globals()) # exec ничего не возвращает, только запускает код в виде строки
    exec(code_str, locals()) # может принимать как глобальный, так и локальный словарь переменных 2-м аргументом

inner()


code_obj = compile("print('Hello from compiled!')", 'compiled_file', 'exec')
exec(code_obj)
