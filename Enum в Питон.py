

from enum import Enum

class Weapon(Enum):  # Объявляем класс-наследник enum.Enum
    SWORD = 1
    BOW = 2
    DAGGER = 3
    CLUB = 4

my_weapon = Weapon.CLUB # Обращение к константе перечисления через точку, как в Java
print(my_weapon)

if my_weapon == Weapon.CLUB:
    print("My weapon is club")

print(list(Weapon)) # Класс enum можно преобразовать в список (является Iterable)

print(Weapon['SWORD'])

print(Weapon(1))

print(type(my_weapon))

print(repr(my_weapon))


# Функциональное создание enum
Weapon = Enum('Weapon', 'SWORD BOW DAGGER CLUB', start=1)
    
weapon = Weapon.DAGGER
print(weapon)
    
if weapon == Weapon.DAGGER:
    print("Dagger")


for weapon in Weapon:
    print(weapon)

for weapon in Weapon:
    print(weapon.name, weapon.value)
