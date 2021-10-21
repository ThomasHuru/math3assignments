from math import *
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def midpointmethod(h,max,start,w,f,y_exact):
    t=start
    w1=w
    w1_arr=[]
    y1exact_arr=[]
    globtrunc = 0.0
    glob_arr = []
    while (t<max):
        globtrunc=abs(y_exact(t)-w1)
        glob_arr = np.append(glob_arr,globtrunc)
        w1_next=w1+h*f(t+h/2,w1+h/2 * f(t,w1))
        w1_arr=np.append(w1_arr,w1)
        y1exact_arr=np.append(y1exact_arr,y_exact(t))
        w1=w1_next
        t=t+h
        print("truncation error: ")
    print("solution: ",w1)
    print("error: ",abs(y_exact(t)-w1))
    plt.plot(w1_arr)
    plt.plot(y1exact_arr)
    plt.plot(glob_arr)
    plt.show()

#midpointmethod(0.1,1,0,1,lambda t,y : t**2*y,lambda t : e**((t**3)/3))

midpointmethod(0.25,1,0,1,lambda t,y : t,lambda t : 1/2*(t**2+2))