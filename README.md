# Matplotlib Graphing with functions

This is a small project going over the basics of graphing through the use of matplotlib and numpy

-----

## Graphs 
### linear_graph.py
- f(x) = sin(x)

![f(x) = sin(x) graph](plots/sinx.png)
- bar chart of data taken from open source NASA dataset

![Planets and their relative orbital periods bar chart](plots/planetbar.png)
- animated graph of f(x) = sin(x) moving from x = 0 to x = pi

![animated f(x) = sin(x)](plots/sinx-anim-scatter.png)
-------
### 3d_graph.py
- 3D graph of f(x,y) = sin(x)cos(y) with colormap

![f(x,y) = sin(x)cos(y)](plots/sinxcosy.png)
------
### particle_motion.py
- Animated motion of particle moving the path: x = t, y = sin(t), z = cos(t) from t \in (-pi, pi)

![particle path graph](plots/particle-mot.png)
------

## Interact with/observe animation of graphs
````bash
git clone https://github.com/koisoysauce/graphing-basics.git
cd graphing-basics
python (file_name)
````
