from matplotlib import pylab as pl
from getworkingpath import *


filnavn = getworkingpath()+'/dobbel.txt'

myfile = pl.loadtxt(filnavn, int)

for i in range(len(myfile)):
     if (myfile[i] != myfile[i-1] and myfile[i] != myfile[i+1]):
        print(myfile[i])

# 724

