import time
import random as rd
import math as mt
import numpy as np



def distance2D(x, y):
    d = np.sqrt(x**(2)+y**(2))
    
    return d

def distance3D(x, y, z):
    r = np.sqrt(x**(2)+y**(2)+z**(2))

    return r

def Pi2D():
    pi = np.pi
    error = 0.1
    inCircle, Total = 0,0
    while (error >= 0.001):
    
        start1 = time.time()
        while True:
            x,y = np.random.random(), np.random.random()
        
            if ((distance2D(x,y))**2 <= 1):
                inCircle += 1
        
            Total += 1
            estimate = 4*inCircle/Total
        
            if abs(estimate/pi-1) <= error:
                print ('{est.} %g vs. {pi} %g after %d trials, {err} %g'%( \
                       estimate,pi,Total,error))
                break
    
        end1 = time.time()    
        print("Elapsed time", end1 - start1,"s\n")
    
        error *= 0.1

def Pi3D():
    pi = np.pi
    error = 0.1
    inCircle, Total = 0,0
    
    while (error >= 0.1):
        x,y,z = np.random.random(), np.random.random(), np.random.random()
        
        start1 = time.time()
        while True:

            if((distance3D(x,y,z)**2 <= 1)):
                inCircle +=1

            Total += 1

            estimate = 6*inCircle/Total

            if abs(estimate/pi - 1) <= error :
                print ('{est.} %g vs. {pi} %g after %d trials, {err} %g'%( \
                       estimate,pi,Total,error))

                break
        
        end1 = time.time() 
        print("Elapsed time", end1 - start1,"s\n")
    
        error *= 0.1


Pi3D()

