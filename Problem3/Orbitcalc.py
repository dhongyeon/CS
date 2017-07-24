import numpy as np
import math as mt
import matplotlib.pyplot as plt
import csv
import seaborn

Gc = 6.67259*(10**(-11))
m = 5.9736*(10**(24))
M = 1.9891*(10**(30))
AU = 1.49597870691*(10**(11))
tscale = 43200


def Initial_Condition():
    Inivec1 = [-9.851920196143998*(0.1)*AU, 1.316466809434336*(0.1)*AU, 4.877392224782687*(10**(-6))*AU]
    Inivec2 = [-9.864337701483683*(0.1)*AU, 1.230799243164879*(0.1)*AU, -4.374019384763304*(10**(-6))*AU]

    return Inivec1, Inivec2

def distance(d):
    d = [(x)**2 for x in d]
    return mt.sqrt(sum(d))

def acceleration(x):
    n = distance(x)

    norm_a = - Gc*M/(n**(3))

    a = [(norm_a)*i for i in x]

    return a

def Kinetic_Energy(x, v):
    vn = [(i)**2 for i in v]
    p = mt.sqrt(sum(vn))

    KE = (0.5)*m*(p**2)

    return KE

def Potential_Energy(x, v):
    n = distance(x)
    
    PE = -Gc*M*m/(n)

    return PE

def Calculation(x):
    i1, i2 = x
    v_initial = [((x2 - x1)/tscale) for x1, x2 in zip(i1,i2)]

    initial_vect = i1
    velocity = v_initial
    T = []
    U = []
    P_vec = []
    
    
    P_vec.insert(0,initial_vect)
    U.insert(0, Potential_Energy(initial_vect, velocity))
    
    position_vec = [(x + v*tscale) for x, v in zip(initial_vect, velocity)]

    P_vec.insert(1, position_vec)
    U.insert(1, Potential_Energy(position_vec, velocity))

    for i in range(2, 730*10+1):
        a = acceleration(position_vec)
        vf = velocity
        velocity= [(vi + ai*tscale) for vi, ai in zip(velocity, a)]
        va = [(i+j) for i, j in zip(velocity, vf)]
        if i == 2:
            vd = [(i*0.5 - j) for i, j in zip(va, vf)]
            
            T.insert(0, Kinetic_Energy([],[(i - j) for i, j in zip(vf, vd)]))

        
        position_vec = [j+(k*tscale) for j, k in zip(position_vec, velocity)]
        P_vec.insert(i, position_vec)
        
        T.insert(i-1, Kinetic_Energy(position_vec, [(i*0.5) for i in va]))
        U.insert(i, Potential_Energy(position_vec, [(i*0.5) for i in va]))

    return P_vec, T, U

def Reverse(x):
    f1, f2 = x[730*10], x[730*10-1]
    return f1, f2

C, T1, U1 = Calculation(Initial_Condition())
D, T2, U2 = Calculation(Reverse(C))

E1 = [i+j for i, j in zip(T1, U1)]
E2 = [i+j for i, j in zip(T2, U2)]

Etotal1 = zip(T1, U1, E1)
Etotal2 = zip(T2, U2, E2)

#Write data in csv
with open("Orbit.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(C)

with open("Energy.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(Etotal1)

with open("Orbit_reverse.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(D)

with open("Energy_reverse.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(Etotal2)

#Open data from csv to plot

with open("Orbit.csv", "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(730*10+1)]
    X = [i[0] for i in fopen] 
    Y = [i[1] for i in fopen]
    Z = [i[2] for i in fopen]

    plt.title("Orbit")
    plt.plot(t, X, label = 'x')
    plt.plot(t, Y, label = 'y')
    plt.plot(t, Z, label = 'z')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('X Y Z')
    plt.savefig("Orbit.png")

f.close()

with open("Energy.csv", "r", newline = "") as g:
    fopen2 = list(csv.reader(g))
    
    t = [i for i in range(730*10)]
    KE = [i[0] for i in fopen2]
    PE = [i[1] for i in fopen2]
    Et = [i[2] for i in fopen2]

    plt.title("Energy")
    plt.plot(t, KE, label = 'KE')
    plt.plot(t, PE, label = 'PE')
    plt.plot(t, Et, label = 'Total')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('Energy(J)')
    plt.savefig("Energy.png")

with open("Orbit_reverse.csv", "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(730*10+1)]
    X = [i[0] for i in fopen] 
    Y = [i[1] for i in fopen]
    Z = [i[2] for i in fopen]

    plt.title("Orbit Reverse")
    plt.plot(t, X, label = 'x')
    plt.plot(t, Y, label = 'y')
    plt.plot(t, Z, label = 'z')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('X Y Z')
    plt.savefig("Orbit Reverse.png")
    

with open("Energy_reverse.csv", "r", newline = "") as g:
    fopen2 = list(csv.reader(g))
    
    t = [i for i in range(730*10)]
    KE = [i[0] for i in fopen2]
    PE = [i[1] for i in fopen2]
    Et = [i[2] for i in fopen2]

    plt.title("Energy Reverse")
    plt.plot(t, KE, label = 'KE')
    plt.plot(t, PE, label = 'PE')
    plt.plot(t, Et, label = 'Total')
    plt.legend(loc='upper left')
    plt.xlabel('time in tscale = 43200 sec')
    plt.ylabel('Energy(J)')
    plt.savefig("Energy Reverse.png")

with open("Orbit.csv", "r", newline = "") as f:
    fopen = list(csv.reader(f))

    t = [i for i in range(730*10+1)]
    X = [i[0] for i in fopen] 
    Y = [i[1] for i in fopen]
    Z = [i[2] for i in fopen]

    plt.title("Orbit")
    plt.plot(X, Y, label = 'y')
    plt.plot(X, Z, label = 'z')
    plt.legend(loc='upper left')
    plt.xlabel('X')
    plt.ylabel('Y, Z')
    plt.gca().set_aspect('equal')
    plt.savefig("Orbit Circle.png")

f.close()