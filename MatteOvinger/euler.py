
import numpy
from math import *
import matplotlib.pyplot as plt
from sympy import Derivative
import sympy as sp
from sympy.core.function import diff
from sympy.core.symbol import Symbol

def euler(h,max,start,w1,w2,f1,f2,y1exact,y2exact):
    t=start
    w1_arr=[]
    w2_arr=[]
    y1exact_arr=[]
    y2exact_arr=[]
    x = Symbol("x")
    globtrunc1 = 0.0
    globtrunc2 = 0.0
    trunc_arr1 = []
    trunc_arr2 = []
    while (t<max):
        globtrunc1 = globtrunc1+abs(y1exact(t)-w1)
        globtrunc2 = globtrunc2+abs(y2exact(t)-w2)
        w1_next=w1+h*f1(w1,w2)
        w2_next=w2+h*f2(w1,w2)
        w1_arr=numpy.append(w1_arr,w1)
        w2_arr=numpy.append(w2_arr,w2)
        y1exact_arr=numpy.append(y1exact_arr,y1exact(t))
        y2exact_arr=numpy.append(y2exact_arr,y2exact(t))
        w1=w1_next
        w2=w2_next
        trunc_arr1=numpy.append(trunc_arr1,globtrunc1)
        trunc_arr2=numpy.append(trunc_arr2,globtrunc2)
        t=t+h
        print(globtrunc1)
    print("solution: ",w1,w2)
    print("error: ",abs(y1exact(t)-w1),abs(y2exact(t)-w2))
    arr = genArr(h,start,max)
    plt.plot(arr,w1_arr)
    plt.plot(arr,y1exact_arr)
    plt.plot(arr,w2_arr)
    plt.plot(arr,y2exact_arr)
    plt.plot(arr,trunc_arr1)
    plt.plot(arr,trunc_arr2)
    plt.show()
def genArr(h,a,b):
    arr = []
    while (a<b):
        arr = numpy.append(arr,a)
        a+=h
    return arr


#euler(0.25 , 1 , 0 , 1 , 0 , lambda a,b : a+b, lambda a,b : -a+b , e ** 1 * cos(1),-e*sin(1))

#euler(0.1 , 1 , 0 , 1 , 0 , lambda a,b : a+b, lambda a,b : -a+b , e ** 1 * cos(1),-e*sin(1))
euler(0.01 , 1 , 0 , 1 , 0 , lambda a,b : a+b, lambda a,b : -a+b ,lambda t :  e ** t * sp.cos(t), lambda t : -e**t*sp.sin(t))
