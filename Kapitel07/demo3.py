import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

x = np.linspace(-np.pi,np.pi,50)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,"k-")
plt.plot(x,y2,"b-")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()