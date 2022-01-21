
print('Введите числов шестнадцатеричной системе для перевода в десятичную')
inp = input()
inp = inp.replace(' ', '')

hex_digits = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

result = 0
for i, digit in enumerate(inp):
    power = len(inp) - 1 - i # Текущая степень, определяемая разрядом цифры
    print(digit)
    if digit in hex_digits:
        result += hex_digits[digit] * 16**power # Умножаем цифру на 16 в текущей степени
    else:
        result += int(digit) * 16**power

print(result)
print('Встроенное преобразование Питон: ', int(inp, base=16)) # Нужно указать kwarg base=16
    
    
