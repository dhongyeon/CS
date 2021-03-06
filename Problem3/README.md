# Yonsei HEP-COSMO Coding Study
## Problem 3
### <div style="text-align: right"> Dhong Yeon Cheong<br>Department of Physics, Yonsei University.

### 1. Ternary Group
* Defined a class to achieve OOP for a Ternary group

* Used the mod calculation to convert the input number into a ternary element. 

```Python
class Ternary_Operation():
    def __init__(self, ternary):
        self.ternary= ternary%3
```
* As the problem stated to use general sum, mult symbols, I overran the +, * symbol as following
```Python
#Operations
def __add__ (self, other): # overrun the addition to use "+"
        sum = self.ternary + other.ternary
        tsum = sum % 3
        
        return Ternary_Operation(tsum)
    
    def __mul__(self, other): #overrun the multiplication to use "*"
        mult = self.ternary * other.ternary
        tmult = mult % 3

        return Ternary_Operation(tmult)

    def __xor__(self, other):
        if self.ternary == 0:
            return "Not defined"

        else:
            if other == 0 : 
                return 1
            
            elif other <0 : 
                return "Not defined"

            else : 
                power = int(other)

                for i in range(1, power+1):
                    self.ternary = self.ternary*self.ternary
                    i = i+1

                return Ternary_Operation(self.ternary % 3)
```
* This allowed me to do normal operations that satisfy group requirements. Finally the results were output via
```python
    def __str__(self):
        return "%i [Ternary]"%(self.ternary)
```

### 2. Orbit Calculation
* The mathematics underlying the numerical calculation of the orbit comes from the definition of acceleration, velocity, and position, which is basically the Taylor expansion

>$$v(t+h) \approx v(t)+ a(t)\bullet h$$ 
>$$ v(t) \approx \frac{s(t+h)-s(t)}{h}$$

* Defined a initial state via
```Python
def Initial_Condition():
    Inivec1 = [-9.851920196143998*(0.1)*AU, 1.316466809434336*(0.1)*AU, 4.877392224782687*(10**(-6))*AU]
    Inivec2 = [-9.864337701483683*(0.1)*AU, 1.230799243164879*(0.1)*AU, -4.374019384763304*(10**(-6))*AU]

    return Inivec1, Inivec2
```

* Defined several useful calculations that will be frequently used
```Python
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
```
* Used these to create a numerical calculation code.

* The main part is the for statement that repeats the integration code, and assigns it to pre-defined lists that act as vectors.
```Python 
def Calculation(x):
    i1, i2 = x
    v_initial = [((x2 - x1)/tscale) for x1, x2 in zip(i1,i2)]

    initial_vect = i1
    velocity = v_initial
    T = []
    U = []
    P_vec = []
    
    
    P_vec.insert(0,initial_vect)
    U.insert(0, Potential_Energy(initial_vect))
    
    position_vec = [(x + v*tscale) for x, v in zip(initial_vect, velocity)]

    P_vec.insert(1, position_vec)
    U.insert(1, Potential_Energy(position_vec))
    
    
    for i in range(2, 7300+1):
        a = acceleration(position_vec)
        v_1step = velocity
        velocity= [(vi + ai*tscale) for vi, ai in zip(velocity, a)]
        
        position_vec = [j+(k*tscale) for j, k in zip(position_vec, velocity)]
        
        P_vec.insert(i, position_vec)
        T.insert(i-1, Kinetic_Energy([(i*0.5) for i in vsum]))
        U.insert(i, Potential_Energy(position_vec))

    return P_vec, T, U
```

* The code also took the boundary cases for the Kinetic energy and assigned them.
```Python
    if i == 2:
            
            T.insert(0, Kinetic_Energy([(i) for i in v_1step]))
            

    elif i == 7300:
           
            
        T.insert(7300, Kinetic_Energy([(i) for i in velocity]))
           
       
    
```

* The resulted graphs are 
<br>
<img src="https://github.com/dhongyeon/CS/blob/master/Problem3/Orbit.png" width=700 height=500>
<img src="https://github.com/dhongyeon/CS/blob/master/Problem3/Plots/Orbit%20Circle.png" width=700 height=500>
<img src="https://github.com/dhongyeon/CS/blob/master/Problem3/Energy.png" width=700 height=500>
<img src="https://github.com/dhongyeon/CS/blob/master/Problem3/Orbit%20Reverse.png" width=700 height=500>
<img src="https://github.com/dhongyeon/CS/blob/master/Problem3/Energy%20Reverse.png" width=700 height=500>