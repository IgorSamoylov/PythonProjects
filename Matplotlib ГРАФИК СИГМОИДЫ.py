import matplotlib.pyplot as plt
import numpy as np

def sigmoida(x):
    return (1 + 2.71828**(-x)) ** -1 # Сигмоида
    

def sigmoida_proizvodn(x):
    return sigmoida(x)  * (1 - sigmoida(x)) # Производная сигмоиды простая

def fermy_dirak_sigmoida(x):
    a = 2
    return 1 / (1 + 2.71828**(-2 * a * x))

def arctangence(x):
    return np.arctan(x)

    


lag = 0.01

x = np.arange(-20.0, 20.0, 0.1)


fig = plt.figure("Построение графиков")

plt.plot(x, sigmoida(x))

plt.plot(x, sigmoida_proizvodn(x))

plt.plot(x, arctangence(x))




plt.text(0, 0,  'Функция', fontsize=18)
plt.title('График функции')
plt.ylabel('Ось Y')
plt.xlabel('Ось Х ')

plt.grid(True)

plt.show()
