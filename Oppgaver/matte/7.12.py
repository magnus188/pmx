from MTmathLib import *
import pylab as pl
import sys, os

def getworkingpath():          
    pathname = os.path.dirname(sys.argv[0])    
    return os.path.abspath(pathname)

filename = getworkingpath() + "./dataset.csv"
dataset = pl.loadtxt(filename,float,delimiter=",", skiprows=1)

time = dataset[:,0]
pos = dataset[:,1]
velocity = []

for i in pos:
    velocity.append((i+1-i)/1)

print(velocity)