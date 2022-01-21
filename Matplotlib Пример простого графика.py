import matplotlib.pyplot as plt
import numpy as np



#w = (1,0.5,0,1)
lag = 0.01
#x = np.arange(0.0, 2*np.pi+lag, lag)
#y = np.cos(x)
x = np.arange(-20.0, 20.0, 0.1)
#y = np.square(x)
y = 1 / (1 + 2.71828**(-x)) # Сигмоида

fig = plt.figure("Построение графиков")
plt.plot(x, y)

plt.text(0, 0,  'Функция', fontsize=18)
plt.title('График функции')
plt.ylabel('Ось Y')
plt.xlabel('Ось Х ')

plt.grid(True)

plt.show()
