import pylab as pl
from MTmathLib import *


N = 10000
deltax = 10E-8

x = pl.arange(0, 101, 0.1)


def f(x):
    return x**2+2*x


print("Derivert: ", newtonsSymmetriske(f, x, deltax))
