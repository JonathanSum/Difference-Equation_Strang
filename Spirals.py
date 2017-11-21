import numpy as np
import matplotlib.pyplot as plt
from numpy import ma

plt.style.use('dark_background')
X, Y = np.meshgrid(np.arange(-10, 10, 0.25*np.pi), np.arange(-10, 10, 0.25*np.pi))
U = -1*((Y-1)*X)
V = -1*((1-X)*Y)
plt.figure()
plt.title('Picture of Solution')
Q = plt.quiver(X, Y, U, V, units='width', color='w', linewidths=(0,))

plt.show()
