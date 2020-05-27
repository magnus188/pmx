import pylab as pl
from getworkingpath import *

filnavn = getworkingpath()+'/juksogfanteri.csv'

myFile = pl.loadtxt(filnavn, float, skiprows=1, delimiter=";")

years = myFile[:, 0]
juks = myFile[:, 1]
fanteri = myFile[:, 2]

diff = juks-fanteri

pl.plot(years, juks, label="Juks", color="blue")
pl.plot(years, fanteri, label="Fanteri", color="orange")
pl.plot(years, diff, label="Differanse", color="green")

pl.axhline(0, color="black")
pl.axvline(years[0], color="black")

pl.title("Juks og fanteri")
pl.xlabel('År')
pl.ylabel('Antall solgt pr år')
pl.legend()
pl.show()
