import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# plt.style.use('dark_background')
fig = plt.figure(figsize = (7, 6))
ax = plt.axes(projection='3d')

# ax.xaxis.pane.set_facecolor((0, 0, 0, 0))
# ax.yaxis.pane.set_facecolor((0, 0, 0, 0))
# ax.zaxis.pane.set_facecolor((0, 0, 0, 0))

# Initiate function f(x, y) = sin(x)cos(y) with cividis colormap
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y) # Returns two 2D arrays for defining our function
Z = np.sin(X) * np.cos(Y)
# Plot function
ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis) # adding _surface covers the space in between lines
# ax.set_aspect('equal')
plt.show()

# Function f(x,y) = sin(sqrt(x ** 2 + y ** 2)) with blue colormap
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

fig = plt.figure(figsize=(7,6))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.Blues)
plt.tight_layout()
plt.show()

# Function f(x,y) = sqrt(x ** 2 + y ** 2 + 1) / hyperboloid of two sheets
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sqrt(X ** 2 + Y ** 2 + 1)
Z2 = -np.sqrt(X ** 2 + Y ** 2 + 1)
fig = plt.figure(figsize=(7,6))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z1, vmin = Z2.min(), vmax = Z1.max(), cmap=plt.cm.Reds)
ax.plot_surface(X, Y, Z2, vmin = Z2.min(), vmax = Z1.max(), cmap=plt.cm.Reds)
plt.tight_layout()
plt.show()
