import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

fig = plt.figure(figsize = (7,7))
ax = plt.axes(projection='3d')
ax.xaxis.pane.set_facecolor((0, 0, 0, 0))
ax.yaxis.pane.set_facecolor((0, 0, 0, 0))
ax.zaxis.pane.set_facecolor((0, 0, 0, 0))
ax.xaxis._axinfo["grid"].update(linewidth=0.1)
ax.yaxis._axinfo["grid"].update(linewidth=0.1)
ax.zaxis._axinfo["grid"].update(linewidth=0.1)

xdata_trail, ydata_trail, zdata_trail = [], [], []
particle, = ax.plot([], [], [], 'bo', markersize=8)
trail, = ax.plot([], [], [], 'b-', alpha=0.5)

ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

def init(): # When the particle reaches the end of the plotting, repeats from this initial state
    xdata_trail.clear()
    ydata_trail.clear()
    zdata_trail.clear()
    
    return particle, trail # Return initialized particle and trail graph

def update(frame): # How does the plot update? For loop through each element in frame (array)
    xdata_trail.append(frame)
    ydata_trail.append(np.sin(frame))
    zdata_trail.append(np.cos(frame))

    particle.set_data([xdata_trail[-1]], [ydata_trail[-1]])
    particle.set_3d_properties([zdata_trail[-1]]) # 3d properties not well integrated in matplotlib, extra function required

    trail.set_data(xdata_trail, ydata_trail)
    trail.set_3d_properties(zdata_trail)

    return particle, trail # Return updated particle and trail graph

ani = FuncAnimation(fig, update, frames=np.linspace(-np.pi, np.pi, 100), init_func=init, blit=False, interval=30)
plt.show()

# Animation of particle free falling in a vacuum closed system
# acceleration of gravity is 9.8 m/s^2
def euler_step(z, step):
    global vel
    vel += step * -9.8
    z.append(z[-1] + step * vel)

def init():
    x.clear()
    x.append(0)
    y.clear()
    y.append(0)
    z.clear()
    z.append(100)
    particle.set_data(x, y)
    particle.set_3d_properties(z)
    trail.set_data(x, y)
    trail.set_3d_properties(z)
    return particle, trail

def update(frame):
    if z[-1] <= 0: # resets simulation when the particle goes below z=0
        init()
        global vel
        vel = 0
        return particle, trail
    
    x.append(0)
    y.append(0)
    euler_step(z, step)
    particle.set_data([x[-1]], [y[-1]])
    particle.set_3d_properties([z[-1]])
    trail.set_data(x, y)
    trail.set_3d_properties(z)
    return particle, trail

x = [0]
y = [0]
z = [100]
vel = 0
step = 0.01
fig = plt.figure(figsize=(7,6))
ax = plt.axes(projection='3d')

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(0, 100)
ax.set_aspect('equal')
ax.xaxis.pane.set_facecolor((0, 0, 0, 0))
ax.yaxis.pane.set_facecolor((0, 0, 0, 0))
ax.zaxis.pane.set_facecolor((0, 0, 0, 0))
ax.xaxis._axinfo["grid"].update(linewidth=0.1)
ax.yaxis._axinfo["grid"].update(linewidth=0.1)
ax.zaxis._axinfo["grid"].update(linewidth=0.1)

particle, = ax.plot(x[-1], y[-1], z[-1], 'bo')
trail, = ax.plot(x, y, z, 'b-', alpha=0.5)

ani = FuncAnimation(fig, func=update, frames=1000, init_func=init, blit=False, interval=50)
plt.tight_layout()
plt.show()
