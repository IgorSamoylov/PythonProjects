
import matplotlib.pyplot as mpl
import numpy as np

x = np.arange(-100.0, 100.0, 1)

print(x)

mpl.plot(x, x**2)

mpl.grid(True)    

mpl.show()
