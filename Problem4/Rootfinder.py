import numpy as np
import math

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
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

    return print(x_after)


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

def bisect(f,x1,x2,switch=0,tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 0.0:
        return x2
    if np.sign(f1) == np.sign(f2):
        print('Root is not bracketed')
        return None
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))
    
    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        
        if (switch == 1) and (abs(f3) >abs(f1)) and (abs(f3) > abs(f2)):
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

def roots(f, a, b, eps=1e-6):
    print ('The roots on the interval [%f, %f] are:' % (a,b))
    
    RMatrix = []
    i = 0
    while True:
        x1,x2 = rootsearch(f,a,b,eps)
        if x1 != None:
            
            a = x2
            root = bisect(f,x1,x2,0)
            if root != None:
                
                r = root
                
                RMatrix.insert(i, r)

                i = i+1
                print(i)
        else:
            return RMatrix
            break

        
    





f = math.sin
print(roots(f, -10, 10))

    

    






