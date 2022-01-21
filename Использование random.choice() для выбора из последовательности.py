
def one_point():
    return "Вам выпало 1 очко!"

def two_point():
    return "Вам выпало 2 очка!"

def three_point():
    return "Вам выпало 3 очка!"

def four_point():
    return "Вам выпало 4 очка!"

def five_point():
    return "Вам выпало 5 очков!"

def six_point():
    return "Вам выпало 6 очков!"


import random

funcs = (one_point, two_point, three_point, four_point, five_point, six_point)

print(random.choice(funcs) ())
