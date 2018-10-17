import numpy as np
import math
import copy

def Cholesky(A):
    n = np.size(A,0)
    for i in range(n):
        for j in range(i,n):
            r = 0
            if (i>0):
                r = np.sum(np.sum(A[0:i,i].T*A[0:i,j]))
            if (i==j):
                A[i,j] = math.sqrt(A[i,j]-r)
            else:
                A[i,j] = (A[i,j]-r)/A[i,i]
                A[j,i] = 0
    B = copy.deepcopy(A)
    for i in reversed(range(n)):
        for j in reversed(range(i,n)):
            x = 0
            if (i<n-1):
                x = np.sum(np.sum(A[i,i+1:]*B[i+1:,j]))
            if (i==j):
                B[i,j] = ((1/A[i,j])-x)/A[i,j]
            else:
                B[i,j] = (0-x)/A[i,i]
                B[j,i] = B[i,j]
    return B

def main():
    print(np.around(Cholesky(np.mat('4. 12. -16.;12. 37. -43.;-16. -43. 98.')),decimals=3))

if __name__ == '__main__':
    main()