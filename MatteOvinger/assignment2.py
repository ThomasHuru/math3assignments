import math
from typing import ItemsView
import numpy
#oppg.6 chpt 1.4
f = lambda x: math.pi*(x**2)*10+(2*math.pi*(x**3)/3)-60
df = lambda x: 20*math.pi*x+2*math.pi*(x**2)

def newton(f,df,epsilon,x0):
    xn=x0
    iteration = 0
    while True:
        xntemp=xn-f(xn)/df(xn)
        iteration+=1
        if (abs(xntemp-xn)<epsilon):
            break
        xn=xntemp
    print("x: ",xn," iterations: ",iteration)
#newton(f,df,0.000001,20)

#oppg 1+2 chpt 2.1
a = numpy.array([[1.0,2.0,-1.0],
                [0.0,3.0,1.0],
                [2.0,-1.0,1.0]])
b2=numpy.array([-1.0,1.0,-3.0])
a2 = numpy.array([[2.0,-2.0,-1.0],
                [4.0,1.0,-2.0],
                [-2.0,1.0,-1.0]])
b = numpy.array([2.0,4.0,2.0])

def makeHilbert(n):
    a = numpy.zeros((n,n))
    for i in range(n):
        for j in range(n):
            a[i,j]=1.0/(i+j+1.0)
    return a
bHilbert = numpy.array([1.0,1.0])
b2Hilbert = numpy.array([1.0,1.0,1.0,1.0,1.0])
b3Hilbert = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])


def gauss(a,b):
    n = len(a)
    x = numpy.zeros(n)
    #elemination
    for i in range(n):
        if a[i,i] == 0:
            print("error divide by zero")
        for j in range(i+1,n):
            mult = a[j,i]/a[i,i]
            for k in range(n):
                a[j,k] = a[j,k]-mult*a[i,k]
            b[j] = b[j] - mult*b[i]
    #back-substitution
    x[n-1] = b[n-1]/a[n-1][n-1]
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            b[i] = b[i] - a[i,j]*x[j]
        x[i] = b[i]/a[i,i]
    for i in range(n):
        print(i," value: ",x[i])
#gauss(a,b)
#gauss(a,b)
#gauss(makeHilbert(2),bHilbert)
#gauss(makeHilbert(5),b2Hilbert)
#gauss(makeHilbert(10),b3Hilbert)
#print(makeHilbert(5))



## Chapter 2.2 cp1 and cp2
b = numpy.array([2.0,4.0,2.0])
a = numpy.array([[1.0,2.0,-1.0],
                [0.0,3.0,1.0],
                [2.0,-1.0,1.0]])

def LuFac(a,b):
    n = len(a)
    Lu = numpy.zeros((n,n))
    for i in range(n):
        Lu[i,i]=1.0
    #elemination
    for i in range(n):
        if a[i,i] == 0:
            print("error divide by zero")
        for j in range(i+1,n):
            mult = a[j,i]/a[i,i]
            for k in range(n):
                a[j,k] = a[j,k]-mult*a[i,k]
            Lu[j,i] = mult
    #Print matrix for CPTP 1
    print("Factorized matrix: ")
    print(a)
    print(Lu)
    #back-substitution
    for i in range(0,n):
        for j in range(i):
            b[i]=b[i]-Lu[i,j]*b[j]
        b[i] = b[i]/Lu[i,i]
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            b[i]=b[i]-a[i,j]*b[j]
        b[i] = b[i]/a[i,i]

    print("Solution: ",b)
        

#LuFac(a,b)


#chpt 2.3 CPTP 6:
a=numpy.array([[10**(-20),1.0],
                [1.0,2.0]])
b=numpy.array([1.0,4.0])

#gauss(a,b)

