import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig = plt.figure(figsize = (7, 7))
ax = plt.axes(projection='3d')
ax.set_aspect('equal')
ax.xaxis.pane.set_facecolor((0, 0, 0, 0))
ax.yaxis.pane.set_facecolor((0, 0, 0, 0))
ax.zaxis.pane.set_facecolor((0, 0, 0, 0))

# Initiate function f(x, y) = sin(x)cos(y)
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
# Plot function
ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

plt.show()