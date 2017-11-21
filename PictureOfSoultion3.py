
import numpy as np
import matplotlib.pyplot as plt
from numpy import ma

X, Y = np.meshgrid(np.arange(-4 * np.pi, 4 * np.pi, 0.25*np.pi), np.arange(-4 * np.pi, 4 * np.pi,0.25*np.pi))
plt.style.use('dark_background')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
t = np.linspace(0, 100, 100)
print(theta)
# U = np.cos(theta)
# V = np.sin(theta)
# plt.figure()
# plt.title('Picture of Solution3')
# Q = plt.quiver(X, Y, U, V, units='width', color='w')
#
# plt.show()
import matplotlib.pyplot as plt
y = t * np.sin(theta)
x = t * np.cos(theta)
plt.plot(x, y)
plt.ylabel('some numbers')
plt.show()