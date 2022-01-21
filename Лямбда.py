
print((lambda x: x * 1000)(777))




lambda_var = lambda t: (t, t % 2 == 0) # Лямбду можно присвоить переменной

import random
data_set = {int(random.random() * 100) for n in range(100)}
print(data_set)
print(*map(lambda_var, data_set))


lambda_m = lambda inp_set: print("-> ", *map(lambda_var, inp_set))
import threading
threading.Thread(target=lambda_m,args=(data_set,)).start()
# В args нужно передавать кортеж, если параметр - последовательность, то, чтобы избежать
# автопреобразования в tuple всей последовательности нужно поставить запятую
