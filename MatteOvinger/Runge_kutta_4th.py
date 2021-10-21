from numpy import *
import numpy
import matplotlib.pyplot as plt

def rungKutta(start,max,h,f,w1,y_exact):
    s1 = lambda t,w : f(t,w)
    s2 = lambda t,w : f(t+h/2,w + h / 2 * s1(t,w))
    s3 = lambda t,w : f(t+h/2,w + h / 2 * s2(t,w))
    s4 = lambda t,w : f(t+h/2,w + h / 2 * s3(t,w))
    w=w1
    t=start
    y_aprox = []
    y_aprox = numpy.append(y_aprox,w)
    globtrunc = 0.0
    glob_arr = []
    globtrunc=abs(y_exact(t)-w)
    glob_arr = numpy.append(glob_arr,globtrunc)
    y1exact_arr=[]
    while (t<max):
        w_next = w + h / 6 * (s1(t,w)+2*s2(t,w)+2*s3(t,w)+s4(t,w))
        w = w_next
        y1exact_arr=numpy.append(y1exact_arr,y_exact(t))
        t +=h
        y_aprox = numpy.append(y_aprox,w)
        globtrunc=abs(y_exact(t)-w)
        glob_arr = numpy.append(glob_arr,globtrunc)
    y1exact_arr=numpy.append(y1exact_arr,y_exact(t))
    arr = genArr(h,start,max)
    plt.plot(arr,y_aprox)
    print("y aprox: ",y_aprox)
    plt.plot(arr,glob_arr)
    print("error: ",glob_arr)
    plt.plot(arr,y1exact_arr)
def genArr(h,a,b):
    arr = []
    while (a<b):
        arr = numpy.append(arr,a)
        a+=h
    arr = numpy.append(arr,a)
    return arr

#rungKutta(0,1,0.5,lambda t,y : t**2*y,1,lambda t : numpy.e**((t**3)/3))
rungKutta(0,1,0.01,lambda t,y : t**2*y,1,lambda t : numpy.e**((t**3)/3))
plt.show()
    
