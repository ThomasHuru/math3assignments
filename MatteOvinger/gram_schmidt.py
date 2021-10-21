import numpy
from numpy import *

def gram_scmidt(matrix):
    retMatrix = []
    n=len(matrix)
    for i in range(n):
        A  = matrix[i]
        y = A
        for j in range(i):
            r = dot(q,A)
            y = y-r*q
        r = numpy.linalg.norm(y)
        print(r)
        q = y / r
        retMatrix.append(q)
    return retMatrix
print(gram_scmidt([[1,2,2],[-4,3,2]]))
def mod_gram_scmidt(matrix):
    retMatrix = []
    n=len(matrix)
    for i in range(n):
        A  = matrix[i]
        y = A
        for j in range(i):
            r = dot(q,y)
            y = y-r*q
        r = numpy.linalg.norm(y)
        print(r)
        q = y / r
        retMatrix.append(q)
    return retMatrix

