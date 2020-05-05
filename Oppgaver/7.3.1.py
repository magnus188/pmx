from MTmathLib import *
import numpy as np

def f(x):
    return x**2-4*x+5

x = np.linspace(0,10,6)

for deltax in range(2,10):
    print(newtonsKvotient(f,x,deltax/10))
