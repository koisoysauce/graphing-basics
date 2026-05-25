import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 2, 100)
y = (t**2)

fig, ax = plt.subplots()

ax.set_xlim([min(t), max(t)])
ax.set_ylim([min(y), max(y)])

animated_plot, = ax.plot([], [])

def update_data(frame):
    animated_plot.set_data(t[:frame], y[:frame])
    return # this makes the graph update the frames rather than showing everything at once,

def init():
    animated_plot.set_data([], [])
    return

animation = FuncAnimation(
            fig=fig, 
            func=update_data,
            frames=len(t),
            interval=30
)

plt.show()

x = np.arange (-1, 1, 0.01)
y = np.arcsin(x)

fig, ax = plt.subplots()

animated_plot, = ax.plot([], [])

def init():
    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([min(y), max(y)])
    animated_plot.set_data([], [])
    return
def update_data(frame):
    animated_plot.set_data(x[:frame], y[:frame])
    return

anim = FuncAnimation(fig=fig, func=update_data, frames=len(x), init_func=init, interval=20)
plt.show()