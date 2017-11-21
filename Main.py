import numpy as np
import matplotlib.pyplot as plt
from numpy import ma

plt.style.use('dark_background')
X, Y = np.meshgrid(np.arange(-2, 2, 0.25), np.arange(-2, 2, 0.25))
U = (1-Y)*X
V =(1-X)*Y
plt.figure()
plt.title('Picture of Solution')
Q = plt.quiver(X, Y, U, V, units='width', color='w', linewidths=(0,))

plt.show()
