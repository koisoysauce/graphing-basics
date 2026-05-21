import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.01)
y = x ** 2
fig, ax = plt.subplots()
ax.plot(x, y)
plt.title("x**2")
plt.show()

np.arcsin
x = np.arange(-1, 1, 0.01)
y = np.arcsin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_ybound(-1, 1)
plt.title("arcsin x")
plt.show()

fig, ax = plt.subplots()
ax.plot(x, x)
plt.show()

# Parameters for standard form: (x^2/a^2) - (y^2/b^2) = 1
a, b = 2, 1
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Define the implicit equation
F = (X**2 / a**2) - (Y**2 / b**2)

# Plot the contour where the equation equals 1
fig, ax = plt.subplots()
ax.contour(X, Y, F, [1], colors='blue')
ax.set_xbound(-10, 10)
ax.set_ybound(-10, 10)
plt.title("Hyperbola")
plt.show()

x = np.array([-2, -1, 0, 1, 2])
y = [2, 1, 0, 1, 2]
plt.plot(x, y, "r-")
plt.show()