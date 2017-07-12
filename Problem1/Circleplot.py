#%%
import numpy as np
import matplotlib.pyplot as plt

from math import sin, cos

r = 1
x = np.linspace(-r,r,1000)
y = np.sqrt(-x**(2)+r**(2))

theta1 = input("Theta value ")
theta1 = float(theta1)
x1 = r*cos(theta1)
y1 = r*sin(theta1)

b = -(x1/y1)*x+(r/y1)

plt.plot(x,y,'b',x,b,'r')
plt.plot(x,-y,'b',x,b,'r')
plt.gca().set_aspect('equal')

plt.show()