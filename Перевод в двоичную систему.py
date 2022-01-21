

print('Введите число')
i = int(input())
k = i

print('От младших разрядов к старшим:')
print('Двоичная система:')
while i > 0:
    print(i % 2)
    i //= 2

print('Шестнадцатеричная система:')
new_digit = ('A', 'B', 'C', 'D', 'E', 'F')
while k > 0:
    d0 = k % 16
    d = d0 if d0 < 10 else new_digit[d0 - 10]
    print(d)
    k //= 16

    
