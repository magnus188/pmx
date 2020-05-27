from MTmathLib import *
import pylab as pl

deltaX = 1E-8
iterations = 10000
x = pl.linspace(2, 5, 3) 


# Define function
def f(x):
    return 2*x+1


print("Newtons Kvotient: ", newtonsKvotient(f, x, deltaX))
print("Newtons Symmetriske: ", newtonsSymmetriske(f, x, deltaX))

