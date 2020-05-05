from matplotlib import pylab as pl
from getworkingpath import *


filnavn = getworkingpath()+'/bokstaver.txt'

myfile = pl.loadtxt(filnavn, str)

word = []

for letter in myfile:
    if (letter.islower()):
        word.append(letter)

print(word)

#covid
