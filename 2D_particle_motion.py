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
'''
important functions to look through documentation:
plt.set()
list.clear()
plt.set_data()
axes.plot() # Works same way as `plt.plot()`, just with the ax variable
list.append()
plt.animation.FuncAnimation()

Sources:
animation example: https://matplotlib.org/stable/users/explain/animations/animations.html
plt.animation.FuncAnimation(): https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html
plt functions: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.plot.html
'''

# TODO: make a particle animation of x = t, y = t ** 2, for t going from 0 to 2
# What t describes how the x-coord and y-coord changes depending on the time, aka the frame
#   So at time t=0, x = 0 and y = 0
#   at time t=2, x = 2 and y = 4
# t goes from 0 to 2, in other words the frame will be an array from 0 to 2

# What the task implies:
# - make a fig and ax along with x and y data as lists
# - make init() function that resets data and updates plot to revert to original state
# - make update(frame) function that defines x and y depending on the frame
# - make an animation using an interval of 30
# - show the animated plot
