import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

plt.style.use('dark_background')

# Graph of sin(x)
x = np.arange(0, 8 * np.pi, 0.01) # This is the independent variable, arange() returns an array from 0 to 8pi with a step of 0.01
plt.plot(x, np.sin(x)) # np.sin(x) is the dependent variable, in esssence: f(x) = sin(x)
plt.xlabel('x') # Labels the x-axis
plt.ylabel('y') # Labels the y-axis
plt.title('f(x) = sin(x)') # Title for the graph
plt.tight_layout() # Makes a tighter layout for better visualization, not necessarily needed
plt.show() # Shows the graph in matplotlib's UI

# Bar chart of planets and their orbital periods, not important
df = pd.read_csv('dataset.csv')
plt.bar(df['planet'], df['orbital_period'])
plt.title('Planets and their relative orbital periods')
plt.tight_layout()
plt.show()

# Most of what we would do would have to do with graphs, specifically animated graphs for visualizing physics concepts
# Animated graph of f(x) = sin(x)
fig, ax = plt.subplots() # fig is figure aka the whole graph, ax is where we input data
xdata, ydata = [], [] # placeholder data for updated points we add through frames
ln, = ax.plot([], [], 'bo') # The data and visualization for plotting
def init(): # initialize graph, what will it look like?
    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-1, 1)
    return ln, # Always return ln, I guess
def update(frame): # Update function, how do I graph the function? What is x and what is y? Update into ln
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln, # Always return ln,

# Call animation function
ani = FuncAnimation(fig, update, frames=np.linspace(-np.pi, np.pi, 100), init_func=init, blit=True, interval=30)
plt.show() # Shows the graph

# Animated circle graph
fig, ax = plt.subplots()
x = []
y = []
ln, = ax.plot(x, y, 'b-')
def init():
    ax.set_xlim(-1.25,1.25)
    ax.set_ylim(-1.25,1.25)
    x.clear()
    y.clear()
    ln.set_data(x, y)
    ax.set_aspect('equal')
    return ln,
def update(frame):
    x.append(-np.cos(frame))
    y.append(np.sin(frame))
    ln.set_data(x, y)
    return ln,

ani = FuncAnimation(fig, func=update, frames=np.linspace(0, 2 * np.pi, 100), init_func=init, interval=30)
ani = FuncAnimation(fig, func=update, frames=np.linspace(0, 2 * np.pi, 100), )
plt.show()
