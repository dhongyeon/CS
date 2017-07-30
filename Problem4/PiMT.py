import time
import random as rd
import math as mt
import numpy as np
import matplotlib.pyplot as plt



def distance2D(x, y):
    d = np.sqrt(x**(2)+y**(2))
    
    return d

def distance3D(x, y, z):
    r = np.sqrt(x**(2)+y**(2)+z**(2))

    return r

def Pi2D():
    pi = np.pi
    error = 0.1
   
    while (error >= 0.0001):
        inCircle, Total = 0,0
        start1 = time.time()
        while True:
            x,y = np.random.random(), np.random.random()
        
            if ((distance2D(x,y)) <= 1):
                inCircle += 1
        
            Total += 1
            estimate = 4*inCircle/Total
        
            if abs(estimate/pi-1) <= error:
                print ('{est.} %g vs. {pi} %g after %d trials, {err} %g'%( \
                       estimate,pi,Total,error))
                break
    
        end1 = time.time()
        plt.show()    
        print("Elapsed time", end1 - start1,"s\n")
    
        error *= 0.1

def Pi3D():
    pi = np.pi
    error = 0.1
    

    while (error >= 0.00000001):
        inCircle, Total = 0,0
        start1 = time.time()
        while True:
            x,y,z = np.random.random(), np.random.random(), np.random.random()
            if((distance3D(x,y,z)<= 1)):
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
