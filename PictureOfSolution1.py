
import numpy as np
import matplotlib.pyplot as plt
from numpy import ma

X, Y = np.meshgrid(np.arange(0, 4, 0.5), np.arange(-2, 4, 0.5))
plt.style.use('dark_background')
U = X
V = Y-Y**2
plt.figure()
plt.title('Picture of Solution')

Q = plt.quiver(X, Y, U, V, units='width', color='w')

plt.show()



# qk = plt.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
#                    coordinates='figure')