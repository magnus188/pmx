import pylab as pl
from getworkingpath import *

filnavn = getworkingpath()+'/Congress_White_House.csv'

myfile = pl.open(filnavn, 'r')
myfile.readline()

for row in myfile:
    data = row.split(';')
    

