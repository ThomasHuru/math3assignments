import math
print("chpt0.1 cp1:")
x=0
for i in range (0,51):
    x=x+1.0000**i
print(x)
x=1.0001
print((x**51-1)/(x-1))

print("chpt 0.4 cp1 a):")
def func(a):
    return ((1 - ( 1/math.cos(a) ) )/(math.tan(a)**2))

def func2(a):
    return (-1/(1+(1/math.cos(a))))

for i in range (1,15):
    value = 10**-i
    print("iteration: ",i)
    print("Original function: ",func(value)," Improved function: ",func2(value))

print("cp5:")
print(1.2222222**2/(math.sqrt(3344556600**2+1.2222222**2)+3344556600))

print("chpt 1.1 cp1:")
def bisection(f,a,b,tol):
    fa = f(a)
    fb = f(b)
    while ((b-a)/2>tol):
        c=(a+b)/2
        fc=f(c)
        if fc == 0:
            break
        if fa*fc<0:
            b=c
        else:
            a=c
    return [a,b]
f = lambda x: x**3-9
print(bisection(f,1,9,0.0001))

print("chpt 1.2 cp1:")
def fixedoint(f,guess):
    x1=f(guess)
    while True:
        x2=f(x1)
        if (x2 == x1):
            return x1
        x1=x2

print("a)")
print(fixedoint(lambda x: (2*x+2)**(1/3),0.4))
print("b)")
print(fixedoint(lambda x: math.log(7-x),5))
print("c)")
print(fixedoint(lambda x: math.log(4-math.sin(x)),5))