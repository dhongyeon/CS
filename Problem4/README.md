# Yonsei HEP-COSMO Coding Study
## Problem 4
### <div style="text-align: right"> Dhong Yeon Cheong<br>Department of Physics, Yonsei University.
<br>

#### 1. Monte-Carlo Method for calculating Pi
<br>

* Used two methods, a circle system & a sphere system. 

* For the 2D system, I generated 2 random numbers in the range (0, 1) and used probability rules to determine $\pi$. $$Prob = \frac{\pi}{4} :=> \pi = 4 \bullet Prob$$
$$ \pi = 4\times \frac{Inside \ Count}{Total\ Count}$$
The code corresponding to this algorithm is 
```Python
        while True:
            x,y = np.random.random(), np.random.random()
        
            if ((distance2D(x,y)) <= 1):
                inCircle += 1
        
            Total += 1
            estimate = 4*inCircle/Total
```
* As the problem required 10%, 1%, 0.1% accuracy, I used a while statement that repeats the computing until the designated error.

* For the 3D case, I used an octant, took 3 random numbers in (0,1), used probability rules to determine the value of $\pi$.$$ Prob = \frac{\frac{4}{3}\pi r^3}{8r^3} :=> \pi = 6Prob $$ $$\pi = 6 \times \frac{Inside\ Count}{Total\ Count}$$
```Python
        while True:
            x,y,z = np.random.random(), np.random.random(), np.random.random()
            if((distance3D(x,y,z)<= 1)):
                inCircle +=1

            Total += 1

            estimate = 6*inCircle/Total
```
<br>
#### 2. Root Finder
1) Newtonian Method
The Newtonian method of calculating zeros of an equation uses the fact that the $x$ intercept of the tangent line of $x_0$ are similar. Consider the Taylor expansion $$f(x_{i+1}) = f(x_i) + f'(x_i)(x_{i+1} - x_1) + ...$$
If we solve this for $x_{i+1}$ assuming $x_i$ is close to $x_{i+1}$, we get the formula, $$x_{i+1} = x_{i} - \frac{f(x_i)}{f'(x_{i})}$$
This was implicated into Python via
```Python
def Derivative(f, x, h):
    deriv = (f(x+h)-f(x-h))/(2.0*h)
    return deriv

def Newtonian(f, x_0, accuracy):
    x_before = x_0
    y = f
    df = Derivative(f, x_before, 1.e-9)
    x_after = x_before - (f(x_0)/(df))
    
    while (abs(x_after-x_before)>accuracy):
        x_before = x_after
        x_after = x_before - (f(x_before)/(Derivative(f, x_before, 1.e-9)))


    return (x_after)
```
2) Bisection Method.
This uses the fact that for a function $y = f(x)$ where its values $f(a)f(b) < 0$ the equation $f(x)=0$ has at least one root in that boundary. And by closing the boundary into an infinitesimal size, we can determine the value of the root. To improve the computing time, I considered the following steps.
    * 


