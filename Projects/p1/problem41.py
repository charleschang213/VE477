def Karatsuba(a,b,n):
    if (a==0) or (b==0):
        return 0
    if (n==1):
        return a*b
    sign = 1
    if (a<0):
        a = a*-1
        sign = sign*-1
    if (b<0):
        b = b*-1
        sign = sign*-1
    half = n/2
    a1 = int(a/(10**half))
    b1 = int(b/(10**half))
    a2 = a%(10**half)
    b2 = b%(10**half)
    U = Karatsuba(a1,b1,half)
    V = Karatsuba(a2,b2,half)
    W = Karatsuba(a1-a2,b1-b2,half)
    Z = U+V-W
    return sign*((U*(10**n))+(Z*(10**half))+V)

def main():
    print(int(Karatsuba(12345678,87654321,8)))
    print(12345678*87654321)

if __name__ == '__main__':
    main()