import numpy as np
import math as mt
import scipy as sc
import pandas as pd

Gc = 6.67259*(10**(-11))
m = 5.9736*(10**(24))
M = 1.9891*(10**(30))
AU = 1.49597870691*(10*(11))
tscale = 43200


def Initial_Condition():
    Inivec1 = np.array([-9.851920196143998*(0.1)*AU, 1.316466809434336*(0.1)*AU, 4.877392224782687*(10**(-6))*AU])
    Inivec2 = np.array([-9.864337701483683*(0.1)*AU, 1.230799243164879*(0.1)*AU, -4.374019384763304*(10**(-6))*AU])

    return Inivec1, Inivec2

print(Initial_Condition())
