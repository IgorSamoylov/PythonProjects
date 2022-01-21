i = 5
while i < 15:
   print(i)
   i = i + 2

while True:
    print('Стук-стук')
    answer = input()
    if answer == 'кто там?':
        print('Миша')
        break
    else:
        continue
