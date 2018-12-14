import random
import time

def RandomSearch(A,k):
    n = len(A)
    checked = [0 for i in range(n)]
    while sum(checked)!=n:
        i = random.randint(0,n-1)
        if (A[i]==k):
             return i
        checked[i] = 1
    return -1

def LinearSearch(A,k):
    n = len(A)
    for i in range(n):
        if (A[i]==k):
            return i
    return -1

def ScrambleSearch(A,k):
    random.shuffle(A)
    n = len(A)
    for i in range(n):
        if (A[i]==k):
            return i
    return -1

def main():
    A = [random.randint(1,100000000)for i in range(100000000)]
    k = random.randint(1,100000000)
    start = time.time()
    print(LinearSearch(A,k), "time:",time.time()-start)
    start = time.time()
    print(RandomSearch(A,k), "time:",time.time()-start)
    start = time.time()
    print(ScrambleSearch(A,k),"time:",time.time()-start)

if __name__ == '__main__':
    main()
