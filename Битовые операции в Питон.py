

# Побитовое НЕ, меняет знак числа (поскольку меняет старший бит в int)
n = 0b111111
r =~n
print(bin(n),'НЕ', bin(r))

n = 0b111111
k = 0b000011

# Побитовое И
r = n & k
print(bin(n),'И',bin(k),'=',bin(r))

# Побитовое ИЛИ
r = n | k
print(bin(n),'ИЛИ',bin(k),'=',bin(r))

# Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ
r = n ^ k
print(bin(n),'ИСКЛЮЧАЮЩЕЕ ИЛИ',bin(k),'=',bin(r))

# Побитовый СДВИГ ВПРАВО
r = n >> k
print(bin(n),'СДВИГ ВПРАВО на',k,'=',bin(r))

# Побитовый СДВИГ ВЛЕВО
r = n << k
print(bin(n),'СДВИГ ВЛЕВО НА',k,'=',bin(r))
