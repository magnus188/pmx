from MTmathLib import *
import numpy as np

deltaX = 10**-8
iterations = 10000
x = np.linspace(0, 10, 6) # Hvorfor??


# Define function
def f(x):
    return 2*x**2+x-5


print("Newtons Kvotient: ", newtonsKvotient(f, x, deltaX))
print("Newtons Symmetriske: ", newtonsSymmetriske(f, x, deltaX))
