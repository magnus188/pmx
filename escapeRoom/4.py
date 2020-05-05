from matplotlib import pylab as pl
from getworkingpath import *


filnavn = getworkingpath()+'/primtall.txt'

myfile = pl.loadtxt(filnavn, int)

for num in myfile:
    for i in range(2, num):
        if (num%i == 0):
            print(num) 
    
#623