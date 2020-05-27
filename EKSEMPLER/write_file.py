import pylab as pl
from getworkingpath import *


filePath = getworkingpath()+'filename.txt'

myFile = open(filePath, 'w')  # w står for write
myFile.write('Hello this is \n magnus')
myFile.close()
