import random
import numpy

def Matrix_multip(M1,M2):
    M = numpy.zeros((5, 5))
    for i in range(5):
        for j in range(5):
            for k in range(10):
                M[i][j]+=M1[i][k]*M2[k][j]
    return M

if __name__ == '__main__':
    M1=numpy.zeros((5,10))
    M2=numpy.zeros((10,5))
    for i in range(5):
        for j in range(10):
            M1[i][j]=random.randint(0,50)
            M2[j][i]=random.randint(0,50)
    for i in range(5):
        for j in range(10):
            print(M1[i][j],end=" ")
        print('\n')
    print('\n')
    for i in range(10):
        for j in range(5):
            print(M2[i][j],end=" ")
        print('\n')
    print('\n')
    M=Matrix_multip(M1,M2)
    for i in range(5):
        for j in range(5):
            print(M[i][j],end=" ")
        print('\n')
