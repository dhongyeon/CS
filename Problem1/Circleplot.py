import numpy as np
import matplotlib.pyplot as plt

r = 1
x = np.linspace(-r,r,1000)
y = np.sqrt(-x**(2)+r**(2))

theta1 = 2.17
x1 = r*np.cos(theta1)
y1 = r*np.sin(theta1)

b = -(x1/y1)*x+(r/y1)

plt.plot(x,y,'b',x,b,'r')
plt.plot(x,-y,'b',x,b,'r')
plt.gca().set_aspect('equal')