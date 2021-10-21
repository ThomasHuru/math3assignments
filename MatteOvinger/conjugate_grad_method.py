
from numpy import *
import numpy

def jacobi(a,b):
    n=len(b)
    d=diag(a)
    r=a-diagflat(d)
    x=zeros(n)
    error = 1.0
    iter = 0
    while((error > 0.0000005)):
        x=(b-dot(r,x)) / d
        error = linalg.norm(b-dot(a,x),numpy.inf)
        iter=iter+1
    print("error: ",error)
    print("iterations: ",iter)
def makeArray(n):
    a=zeros((n,n))
    for i in range(n-1):
        a[i,i]=3
        a[i+1,i]=-1
        a[i,i+1]=-1
    a[n-1,n-1]=3
    return(a)
def makeSol(n):
    a=zeros(n)
    a[0]=2
    for i in range(1,n-1):
        a[i]=1
    a[n-1]=2
    return(a)
def calcBackwarderror(a,est,sol):
    return linalg.norm(sol-a*est)

jacobi(makeArray(100),makeSol(100))

## Conjugate gradient method

def conGradMeth(A,b,M,x0):
    x = x0
    r = b-dot(A,x)
    invM = linalg.inv(M)
    d = invM @ r
    z = d
    n=len(b)
    for i in range(n):
        if (r[0] == 0): break
        a = dot(numpy.transpose(r),z)/dot(numpy.transpose(d), dot(A,d))
        x=x+a * d
        r0=r
        r=r-dot(a , dot(A,d))
        z0=z
        z=dot(invM, r)
        beta = dot(numpy.transpose(r), z) /dot(numpy.transpose(r0) , z0)
        d=z+beta * d
    print(x)
    return(x)
a2=array([[1.0,2.0],[2.0,5.0]])
b2=array([1.0,1.0])
M=array([[sqrt(2)-1,-1-sqrt(2)],[1.0,1.0]])
x0=[1.0,1.0]

##conGradMeth(a2,b2,M,x0)
