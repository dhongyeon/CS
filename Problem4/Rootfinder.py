import numpy as np
import math
import scipy.special as sp

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


    return (x_after)


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
    n = int(math.ceil(np.log(abs(x2 - x1)/tol)/np.log(2.0)))
    
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

def Ai(x):
    (ai, ai_prime, bi, bi_prime) = sp.airy(x)
    return ai

def Function1(x):
    return x - np.cos(x)

print("Newtonian Method for x^2 - 4 = 0, x_0 = 1:", Newtonian(Polynomial([-4,0,1]), 1, 1e-10))
print("Bisection Method for x^2 - 4 = 0 in [-1, 4] :", roots(Polynomial([-4,0,1]), -1, 4),"\n")

print("Newtonian Method for x^5 -2x^3-7x^2+14 = 0, x_0 = 1:", Newtonian(Polynomial([14, 0, -7, -2, 0, 1]), 1, 1e-10))
print("Bisection Method for x^5 -2x^3-7x^2+14 = 0 in [-3,1]:", roots(Polynomial([14, 0, -7, -2, 0, 1]), -3, 1))

print("Every root in [-100, 100] for x-cos(x)=0 : ", roots(Function1, -100, 100))

print("Every root in [-150, 30] for Ai(x) : ", roots(Ai, -150, 30))