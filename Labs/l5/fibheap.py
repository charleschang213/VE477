import math
class Node:
    key = 0
    degree = 0
    p = 0
    child = 0
    left = 0
    right = 0
    value = 0
    mark = False
    def __init__(self,key,value=0):
        self.key = key
        self.value=value
        self.degree = 0
        self.p = 0
        self.child = 0
        self.left = 0
        self.right = 0
        self.mark = False
    def Addchild(self,c):
        c.p = self
        self.degree = self.degree+1
        if self.child==0:
            self.child = c
            c.left = c
            c.right = c
        else:
            tmp = self.child
            c.right = tmp
            c.left = tmp.left
            c.left.right = c
            tmp.left = c
    def SearchChild(self,key):
        w = self
        v = self
        result = 0
        while True:
            if w.key==key:
                return w
            if w.child!=0:
                result = w.child.SearchChild(key)
            if result!=0:
                return result
            w = w.right
            if w==v:
                return 0
    def PrintNode(self):
        if self.child!=0:
            c = self.child
            l = c.left
            while True:
                print("%d has child: %d" % (self.key,c.key))
                c.printNode()
                if l==c:
                    break
                c = c.right

class Fibheap:
    size = 0
    minnode = 0
    def __init__(self,size,minnode):
        self.size = size
        self.minnode = minnode
    def Insert(self,x):
        if self.minnode==0:
            self.minnode=x
            x.left = x
            x.right = x
        else:
            x.right = self.minnode
            x.left = self.minnode.left
            x.left.right = x
            self.minnode.left = x
            if x.key<self.minnode.key:
                self.minnode = x
        self.size = self.size+1
    def Minimum(self):
        return self.minnode
    def Link(self,y,x):
        y.right.left=y.left
        y.left.right=y.right
        y.p=x
        x.degree=x.degree+1
        y.mark=False
        if x.child==0:
            x.child=y
            y.left=y
            y.right=y
        else:
            c=x.child
            y.right=c
            y.left=c.left
            y.left.right=y
            c.left=y
    def Consolidate(self):
            A = []
            for i in range(0,int(math.log(self.size,2)+1)):
                A.append(0)
            w = self.minnode
            t = w.left
            while True:
                x = w
                #print('is %d' % w.key)
                d = x.degree
                while A[d]!=0:
                    y = A[d]
                    if x.key>y.key:
                        v = x 
                        x = y
                        y = v
                    self.Link(y,x)
                    A[d]=0
                    d = d+1
                A[d] = x
                if w==t:
                    break
                w = x.right
            self.minnode=0
            for i in range(0,int(math.log(self.size,2)+1)):
                if A[i]!=0:
                    if self.minnode==0:
                        self.minnode=A[i]
                        A[i].left=A[i]
                        A[i].right=A[i]
                    else:
                        A[i].right=self.minnode
                        A[i].left=self.minnode.left
                        A[i].left.right=A[i]
                        self.minnode.left=A[i]
                        if A[i].key<self.minnode.key:
                            self.minnode=A[i] 
    def ExtractMin(self):
        z = self.minnode
        if z!=0:
            if z.child!=0:
                c = z.child
                while c.p!=0:
                    cpr = c.left
                    cpr.right = c.right
                    c.p = 0
                    c.left = 0
                    c.right = 0
                    c.right = self.minnode
                    c.left = self.minnode.left
                    c.left.right = c
                    self.minnode.left=c
                    c = cpr
            z.right.left = z.left
            z.left.right = z.right
            z.child=0
            if z==z.right:
                self.minnode=0
            else:
                self.minnode=z.right
                self.Consolidate()
            self.size = self.size-1
            return z
    def Cut(self,x,y):
        if y.degree==1:
            y.child=0
            x.p=0
        else:
            if x==y.child:
                w=x.right
                w.left=x.left
                x.left.right=x.right
                y.child=w
            else:
                w=y.child
                w.left=x.left
                x.left.right=x.right
        y.degree=y.degree-1
        x.right=self.minnode
        x.left=self.minnode.left
        x.left.right=x
        self.minnode.left=x
        if x.key<self.minnode.key:
            self.minnode=x
        x.p=0
        x.mark=False
    def CasCut(self,y):
        while y.p!=0 and y.mark==True:
            parent = y.p
            self.Cut(y,parent)
            self.Insert(y)
            y = parent
        if y.parent!=0:
            y.mark=True
    def DecreaseKey(self,x,k):
        if k>x.key:
            print("error: new key is greater than current key")
        x.key=k
        y=x.p
        if y!=0 and x.key<y.key:
            self.Cut(x,y)
            #self.CasCut(y)
        if x.key<self.minnode.key:
            self.minnode=x
    def Delete(self,x):
            self.DecreaseKey(x,-1)
            self.ExtractMin()

def MakeHeap():
    return Fibheap(0,0)

def Union(h1,h2):
    h = MakeHeap()
    if (h1.minnode==0) or h1.minnode.key>h2.minnode.key:
        h.minnode = h2.minnode
    else:
        h.minnode = h1.minnode
    h.size = h1.size+h2.size
    if h1.minnode!=0 and h2.minnode!=0:
        r = h1.minnode.right
        h1.minnode.right = h2.minnode
        h2.minnode.left.right=r
        r.left = h2.minnode.left
        h2.minnode.left=h1.minnode
    return h

def main():
    A = range(1,20,2)
    B = range(0,19,2)
    H1 = MakeHeap()
    H2 = MakeHeap()
    ps = []
    for i in range(len(A)):
        ps.append(Node(B[i]))
        H2.Insert(ps[len(ps)-1])
        ps.append(Node(A[i]))
        H1.Insert(ps[len(ps)-1])
    H1.ExtractMin()
    H1.ExtractMin()
    H1.ExtractMin()
    H2.ExtractMin()
    H2.ExtractMin()
    H2.ExtractMin()
    NH = Union(H1,H2)
    NH.DecreaseKey(ps[9],2)
    NH.Delete(ps[6])
    NH.ExtractMin()
    NH.ExtractMin()
    print(NH.Minimum().key)

if __name__=='__main__':
    main()