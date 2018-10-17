import numpy as np
import copy

def BackwardVector(A):
    n = np.size(A,0)
    if (n==1):
        return np.mat(1/A[0,0])
    b = BackwardVector(A[1:,1:])
    b = np.row_stack((np.zeros(1),b))
    f = np.flipud(b)
    dn = np.sum(np.sum(A[n-1,:]*f))
    d1 = np.sum(np.sum(A[0,:]*b))
    b = 1./(1.-d1*dn)*b-d1/(1.-d1*dn)*f
    return b

def LevinsonDurbin(A):
    n = np.size(A,0)
    if (n==1):
        A[0,0] = 1/A[0,0]
        return A
    B = LevinsonDurbin(A[0:n-1,0:n-1])
    B = np.row_stack((B,np.zeros(n-1)))
    B = np.column_stack((B,BackwardVector(A)))
    for i in range(n-1):
        d = np.sum(np.sum(A[n-1,:]*B[:,i]))
        B[:,i] = B[:,i]-d*B[:,n-1]
    return B

def main(): 
    print(np.around(LevinsonDurbin(np.mat('1. 8. 3. 2. 5. ;8. 1. 8. 3. 2. ;3. 8. 1. 8. 3. ;2. 3. 8. 1. 8. ;5. 2. 3. 8. 1.')),decimals=3))

if __name__ == '__main__':
    main()