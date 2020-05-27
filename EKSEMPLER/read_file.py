import pylab as pl
from getworkingpath import *

#### METODE 1
filePath = getworkingpath()+'filename.txt'

myFile = open(filePath, 'r')  # r står for read
myFile.readline() # Hopp over første linje

for row in myFile:
    data = row.split() # lager liste med dataen. f.eks. data[0], data[1] osv.
    print(data[0])

#### METODE 2

myFile = pl.loadtxt(filePath, float, skiprows=1, delimiter=";")

column1 = myFile[:, 0]
column2 = myFile[:, 1]
column3 = myFile[:, 2]
