
def func(name, time):
    def greeter():
        print(f"Hello, {name}!")
    def buyer():
        print(f"Buy, {name}!")
    if 8 <= time < 17:
        return greeter
    else:
        return buyer


f = func("Igor", 11)
f()
