# Более явная замена рекурсии с использованием замыкания внутренней функции на исходных
# параметрах


def factorial_closures():
    result = 1
    f = 1

    def factorial():
        nonlocal result
        nonlocal f
        result *= f
        f += 1
        return result

    return factorial


factor = factorial_closures()

for i in range(70):
    print(f"{i + 1}! = ", factor())
