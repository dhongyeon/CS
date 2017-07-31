import math
import numpy as np
import csv

with open('/users/Dhong-Yeon/Documents/CS/Problem3/Problem3/Orbit.csv', "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(7300+1)]
    X = [float(i[0]) for i in fopen] 
    Y = [float(i[1]) for i in fopen]
    Z = [float(i[2]) for i in fopen]
    
Distance = [np.sqrt(i**2 + j**2 + k**2) for i, j, k in zip(X, Y, Z)]

def Average(x):
    average = sum(x)/len(x)
    return average


def Midpointfilter(x):
    i = 0
    j = 0
    Ima = []
    for i in range(len(x)):
        if (x[i]>=Average(x)):
            
            element = x[i]
            Ima.append(x[i])

       
    
    return Ima

def localmaxima(x):
    localmaxima = []
  
    for i in range(len(x)):     
        if x[i] > x[i-1] and x[i] > x[i+1]:
            localmaxima.append(x[i])
    return localmaxima
        


print(localmaxima(Midpointfilter(Distance)))
print(max(localmaxima(Midpointfilter(Distance))))






    
