import matplotlib.pyplot as plt
from math import sin, pi

x=[]
y=[]
for i in range(0,101):
    value= i/(100/(2*pi))-pi
    x.append(value)
    y.append(sin(value))

plt.plot(x, y,"k--")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()