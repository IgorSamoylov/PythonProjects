spisok = [10, 20, 30, 40]

for i in spisok:
    print(i + 2)

i = 0

while i < len(spisok):
    print (spisok[i])
    i += 1

for i in range(-10, 10, 2):
    print(i)

for item in enumerate(spisok):
    print(item[0], item[1])

for nomer, znachenie in enumerate(spisok):
    print(nomer, znachenie)

for i in "pidorok":
    print(i)

e_obj = enumerate(spisok)

for i in e_obj:
    if i [1] == 30:
        break
    print(i)


