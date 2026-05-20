import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.01)
y = x ** 2
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()