import numpy
from numpy import *
from numpy.linalg.linalg import norm

def pow_iteration(A,x,k):
    for i in range(k):
        u = x / norm(x)
        x = linalg.dot(A,u)
        λ = linalg.dot(u,x)
    return u