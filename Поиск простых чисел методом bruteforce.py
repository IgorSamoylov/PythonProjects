

def is_prime_number(x):
    """Проверяет, является ли x простым"""
    divider = 2
    while divider < x**0.5:  # Проверяем делители только до sqrt(x)!
        if x % divider == 0:
            return False
        divider += 1
    return True


prime_number_list = []
for i in range(2, 2_000):
    if is_prime_number(i):
        prime_number_list.append(i)

print(prime_number_list)


def main_aryphmetic_theory_test(t):
    """ Проверяет правильность главной теоремы арифметики:
        Все целые числа являются или простыми или представимы как произведение
        простых делителей, причем единственным образом
    """
    if t in prime_number_list:
        return t
    
    divider_list = []
    while t > 1:
        for prime_number in prime_number_list:
            if t % prime_number == 0:
                divider_list.append(prime_number)
                t //= prime_number
                break
        if t in prime_number_list:
            divider_list.append(t)
            break
    return divider_list


for i in range(1000, 1100):
    print('Делители', i, main_aryphmetic_theory_test(i))


def factorize_number(x):
    """ Раскладывает x на множители """
    result_list = []
    divider = 2
    min_value = x**0.5
    while x > 1:
        if x % divider == 0:
            result_list.append(divider)
            x //= divider
        else:
            divider += 1
        if divider > min_value:
            break
    return result_list
    
