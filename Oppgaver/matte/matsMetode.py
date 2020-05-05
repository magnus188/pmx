from pylab import *
import math


A=[3,10,20,30,100,300]
for N in A:
    start=0
    slutt=3
    dx = ((slutt-start)/(N-1))
    x=zeros(N)
    y=zeros(N)
    yder=zeros(N)
    
    x[0]=0
    y[0]=1
    yder[0]=y[0]

    #Resten
    for i in range(1,N):
        x[i]=x[i-1]+dx
        y[i]=dx*yder[i-1]+y[i-1]
        yder[i]=y[i]
    plot(x,y)
def f(x):
    return math.e**x

plot(x,f(x))
