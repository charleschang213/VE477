import numpy as np

def Pivot(N,B,A,b,c,v,l,e):
    bp = np.zeros(len(b))
    bp[e] = b[l]/A[l,e]
    ap = np.zeros([np.size(A,0),np.size(A,1)])
    for j in N:
        ap[e,j]  = A[l,j]/A[l,e]
    ap[e,l] = 1/A[l,e]
    for i in B:
        if i==l:
            continue
        bp[i] = b[i]-A[i,e]*bp[e]
        for j in N:
            if j==e:
                continue
            ap[i,j] = A[i,j] - A[i,e]*ap[e,j]
        ap[i,l] = -1*A[i,e]*ap[e,l]
    v = v+c[e]*bp[e]
    cp = np.zeros(len(c))
    for j in N:
        if j==e:
            continue
        cp[j] = c[j]-c[e]*ap[e,j]
    cp[l] = -1*c[e]*ap[e,l]
    N.remove(e)
    N.append(l)
    B.remove(l)
    B.append(e)
    return N,B,ap,bp,cp,v

def simp_init(A,b,c):
    dual = False
    if (np.size(A,0)>np.size(A,1)):
        A = np.transpose(A)*-1
        tmp = b;b=-1*c;c=-1*tmp
        dual = True
    m = np.size(A,0)
    n = np.size(A,1)
    v = 0
    N = [i for i in range(n)]
    B = [n+i for i in range(m)]
    c = np.hstack((c,[0 for i in range(m)]))
    b = np.hstack(([0 for i in range(n)],b))
    A = np.vstack((np.zeros([n,m+n]),np.hstack((A,np.zeros([m,m])))))
    k = np.where(b==b.min())[0][0]
    if (b[k]>=0):
        return N,B,A,b,c,v,dual
    cp = np.zeros(m+n+1)
    cp[-1] = -1
    A = np.hstack((A,np.zeros([m+n,1])))
    for i in B:
        A[i,m+n] = 1
    l = n+k
    N.append(m+n)
    b = np.hstack((b,[0]))
    N,B,A,b,cp,v = Pivot(N,B,A,b,cp,v,l,0)
    while len(N)!=0 and c.max()>0:
        e = np.where(cp==cp.max())[0][0]
        d = np.zeros(m+n+1)
        for i in range(m+n+1):
            if i in B and A[i,e]>0:
                d[i] = b[i]/A[i,e]
            else:
                d[i] = float("inf")
        l = np.where(d==d.min())[0][0]
        if d[l]!=float("inf"):
            N,B,A,b,cp,v = Pivot(N,B,A,b,cp,v,l,e)
        else:
            return float("inf")
    if (b[m+n]!=0):
        return -1,-1,-1,-1,-1,-1,-1
    if (m+n) in B:
        N,B,A,b,cp,v = Pivot(N,B,A,b,cp,v,m+n,N[0])
    A = A[0:(m+n),:]
    b = b[0:(m+n)]
    for i in B:
        for j in range(m+n):
            c[j] = c[j]+c[i]*A[i,j]
        c[i] = 0
    return N,B,A,b,c,v,dual
    


def simplex(A,b,c):
    m = np.size(A,0)
    n = np.size(A,1)
    N,B,A,b,c,v,dual = simp_init(A,b,c)
    if dual:
        tmp=m;m=n;n=tmp
    while len(N)!=0 and c.max()>0:
        e = np.where(c==c.max())[0][0]
        d = np.zeros(m+n)
        for i in range(m+n):
            if i in B and A[i,e]>0:
                d[i] = b[i]/A[i,e]
            else:
                d[i] = float("inf")
        l = np.where(d==d.min())[0][0]
        if d[l]!=float("inf"):
            N,B,A,b,c,v = Pivot(N,B,A,b,c,v,l,e)
        else:
            return float("inf")
    if not dual:
        x = [0 for i in range(n)]
        for i in range(n):
            if i in B:
                x[i] = b[i]
            else:
                x[i] = 0
        return x,v
    else:
        x = [0 for i in range(m)]
        for i in range(m):
            if n+i in N:
                x[i] = -1*c[n+i]
            else:
                x[i] = 0
        return x,-1*v


def main():
    b = np.array([-6,-14,-13])
    A = np.matrix([[-0.5,-1],[-2,-2],[-1,-4]])
    c = np.array([-24,-60])
    print(simplex(A,b,c))

if __name__=='__main__':
    main()