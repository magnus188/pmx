from MTmathLib import *
import numpy as np

def f(x):
    return x**2

der = newtonsKvotient(f,2,0-10**-8)
print(der)

