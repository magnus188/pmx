# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:29:42 2020

@author: sander1007
"""
#import numpy as np
from pylab import *

######   DERIVASJON


def newtonskvotient(f, x, delta_x):
    fder = (f(x+delta_x)-f(x))/delta_x
    return fder


def newtonssymmetriskekvotient(f, x, delta_x):
    fder = ((f(x+delta_x)-f(x-delta_x))/(delta_x*2))
    return fder

####### INTEGRASJON


# f=funksjon, a=startverdi, b=sluttverdi, n= antall rektangler
def rektangelmetoden(f, a, b, n):
    total = 0.0
    h = (b-a)/n
    for k in range(0, n):
        total += f(a + (k*h))
    areal = h*total
    return areal


def trapesmetoden(f, a, b, n):
    h = (b-a)/n
    total = (f(a)+f(b))/2.0
    for k in range(1, n):
        total += f(a + k*h)
    return h*total


#####   DIFFERENSIALLIKNINGER

def EulersMetode(yder, y0, a, b, N):
    y = zeros(N)
    x = zeros(N)
    h = (b - a)/(N - 1)
    y[0] = y0
    x[0] = a
    for i in range(N - 1):
        y[i+1] = y[i] + h * yder(x[i], y[i])
        x[i+1] = x[i] + h
    return y, x


##### NULLPUNKTER (LIKNINGSLØSER)

def NewtonsMetode(a, tol, N, f, fder):
    #Definerer intervallet
    #    a = Startverdien
    #    tol = Toleransen
    #    N = Antall iterasjoner
    #    f = funksjonen
    #    fder = den deriverte av funksjonen

    i = 1  # Tellevariabel
    c = 1  # Nullpunktsvariabel

    #Newtons metode
    while i <= N and abs(f(c)) >= tol:
        c = a - f(a)/fder(a)
        a = c
        i += 1

    #print('Løsningen på likningen er x =', c, 'og løkka gikk', i, 'ganger')

    return c


def halveringsmetoden(a, b, tol, n, f):

    #a = Startverdi
    #b = Sluttverdi
    #tol = Toleranse
    #n = Antall ganger løkka kan kjøre
    i = 1  # Tellevariabel

    #Halveringsmetoden
    c = (a + b)/2  # Finner første halveringspunkt
    while i < n and abs(f(c)) > tol:
        if f(c) == 0:
            a = b = c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        i += 1
        c = (a + b)/2

    # print('Løsningen på likningen er x =', c, 'og løkka gikk', i, 'ganger')
    return c
