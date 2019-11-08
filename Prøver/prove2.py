import pylab as pl
import sys, os

def getworkingpath():          
    pathname = os.path.dirname(sys.argv[0])    
    return os.path.abspath(pathname)

fileName = getworkingpath()+'/salg.csv'
myFile = pl.loadtxt(fileName,float, skiprows=1, delimiter=";")

years  = myFile[:,0]
gizmo = myFile[:,1]
bobo = myFile[:,3]

pl.plot(years,gizmo, label="Gizmo", color="blue")
pl.plot(years,bobo, label="Bobo", color="orange")

pl.title("Gizmo og Bobo")
pl.xlabel('År')
pl.ylabel('Antall solgt pr år')
pl.legend()
pl.show()