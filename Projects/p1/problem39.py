import numpy as np

def GaussianElimination(A,n):
    prow = 0
    pcol = 0
    B = A
    while (prow<=n-1) and (pcol<=n):
        rmax = np.where(B[prow:,pcol]==np.max(B[prow:,pcol]))[0][0]+prow
        if (B[rmax,pcol]==0):
            pcol = pcol+1
            continue
        B[[prow,rmax],:] = B[[rmax,prow],:]
        for i in range(prow+1,n):
            B[i,:] = B[i,:]-(B[i,pcol]/B[prow,pcol])*B[prow,:]
        prow = prow+1
        pcol = pcol+1
    return B

def main():
    A = np.mat('1.0 2.0 3.0 4.0;4.0 5.0 6.0 7.0;7.0 8.0 9.0 10.0')
    print(np.around(GaussianElimination(A,3),decimals=3))

if __name__ == '__main__':
    main()