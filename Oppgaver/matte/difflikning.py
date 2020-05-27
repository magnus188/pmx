import pylab as pl
import numpy as np

y = [1]
x = [0]
yder = [1]
deltaX = 1

def calculate(x_1):
    global x
    x.append(x_1) 
    y.append(deltaX*y[-1]+y[-1])
    y_der.append(y[-1])


for i in range(1,10):
    calculate(i)

pl.plot(x,y)
pl.show()

print('X:', x)
print('y:', y)
print('y_der:', y)
