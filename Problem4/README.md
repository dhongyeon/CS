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
    * Find The boundaries ($x_1$, $x_2$) for a root.
    * Pass it to a Bisection Method.
    
    To achieve this, I made a root finding code using increments of dx. This function searches for a root of $f(x)$ in the boundary $(a,b)$ in increments of dx. 

```Python
    def rootsearch(f,a,b,dx): #Searches the interval (a,b) in increments dx for the bounds (x1,x2) of the smallest root of f(x).
        x1 = a; f1 = f(a)
        x2 = a + dx; f2 = f(x2)
        while np.sign(f1) == np.sign(f2):
            if x1 >= b:
                return None,None
            x1 = x2
            f1 = f2
        
            x2 = x1 + dx
            f2 = f(x2)
        else:
            return x1,x2
```
Now as we determined the minimal boundary for a root, we can now close this in by using a bisection method. This uses the same logic with the incremental search method. If there is a root between $(x_1, x_2)$, then $f(x_1)$ and $f(x_2)$ have opposite signs. Then we reduce the interval to halve by defining $x_3 = \frac{1}{2}(x_1 + x_2)$, and repeating the process via the preceding rule. 
This is repeated until a small value $\varepsilon$, where $$ |x_2 - x_1| < \varepsilon $$ To achieve this value, note that $|x_2 - x_1|$ is reduced to $2^n$ after n bisections. Thus, by solving for $n$, we get, $$n = \frac{ln(|x_2 - x_1|/\varepsilon)}{ln(2)}$$ To acheive this, we used the ceiling function in numpy. 
The code for Bisection is 
```Python
def bisect(f,x1,x2,tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if np.sign(f1) == np.sign(f2):
        print('No root')
        return None
    
    n = int(math.ceil(np.log(abs(x2 - x1)/tol)/np.log(2.0)))
    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        
        if(abs(f3) >abs(f1)) and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0:
            return x3
        if np.sign(f2) != np.sign(f3) :
            x1 = x3
            f1 = f3
        else:
            x2 =x3
            f2 = f3
    return (x1 + x2)/2.0

```
* The ```if(abs(f3) >abs(f1)) and (abs(f3) > abs(f2))``` part determines whether to check if $f(x)$ decreases upon bisection. If it doesn't, it may be a singularity, thus not a root.  

Now we need to find all the roots of an equation in a given interval. This is achieved by using both ```rootsearch``` and ```bisection```. 
```Python
def roots(f, a, b, eps=0.001):

    RMatrix = []
    i = 0
    while True:
        x1,x2 = rootsearch(f,a,b,eps)
        if x1 != None:
            a = x2
            root = bisect(f,x1,x2,1)
            if root != None:
                r = root 
                RMatrix.insert(i, r)
                
        else:
            return RMatrix
            break
```

3. Maximum Finder.
* Input part
```python 
with open('/users/Dhong-Yeon/Documents/CS/Problem3/Problem3/Orbit.csv', "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(7300+1)]
    X = [float(i[0]) for i in fopen] 
    Y = [float(i[1]) for i in fopen]
    Z = [float(i[2]) for i in fopen]
    
Distance = [np.sqrt(i**2 + j**2 + k**2) for i, j, k in zip(X, Y, Z)]
```
* As the data points are a vast amount, I first created a filter to take only values higher than the average of all points, 
```Python
def Midpointfilter(x):
    Ima = []
    for i in range(len(x)):
        if (x[i]>=Average(x)):
            
            element = x[i]
            Ima.append(x[i])

    return Ima
```
* Then, I used a typical local maximum search algorithm. 
```Python
def localmaxima(x):
    localmaxima = []
  
    for i in range(len(x)):     
        if x[i] > x[i-1] and x[i] > x[i+1]:
            localmaxima.append(x[i])
    return localmaxima
```

#### Reference
* Kiusalaas, Jaan. *Numerical methods in engineering with Python 3*. Cambridge university press, 2013.