import numpy as np

# Сигмоида 
def Nonlinear(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# набор входных данных
X = np.array([          [0,0,1],
                        [0,1,1],
                        [1,0,1],
                        [1,1,1] ])
    
# выходные данные  (T  поворачивает матрицу из горизонтальной в вертикальную)          
y = np.array([[0,0,1,1]]).T

# сделаем случайные числа более определёнными 
np.random.seed(1)

# инициализируем веса случайным образом со средним 0
syn0 = 2*np.random.random((3,1)) - 1
print ("Значения связей до тренировки")
print (syn0)


for iter in range(1000):

    # прямое распространение
    l0 = X
    l1 = Nonlinear(np.dot(l0,syn0))
    if iter%10 == 0:
        print ("Итерация № ",  iter)
        print (l1)
        print ("______________________")
    # насколько мы ошиблись?
    l1_error = y - l1

    # перемножим это с наклоном сигмоиды 
    # на основе значений в l1
    l1_delta = l1_error * Nonlinear(l1,True) 

    # обновим веса
    syn0 += np.dot(l0.T,l1_delta)
    if iter%10 == 0:
        print ("Синапсы: ")
        print (syn0)
        print ("______________________")

print ("Выходные данные после тренировки:")
print (l1)
print ("Значения связей после тренировки")
print (syn0)
