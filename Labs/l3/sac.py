def SortCount(L):
    size = len(L)
    if (size==0) or (size==1):
        return 0
    half = int(size/2)
    rhalf = size-half
    L1 = L[0:half]
    L2 = L[half:size]
    count1 = SortCount(L1)
    count2 = SortCount(L2)
    f1 = f2 = f = 0
    count = count1+count2
    while (f!=size):
        if (f1==half):
            L[f] = L2[f2]
            f2 = f2+1
        elif (f2==rhalf):
            L[f] = L1[f1]
            f1 = f1+1
        elif (L1[f1]<=L2[f2]):
            L[f] = L1[f1]
            f1 = f1+1
        else:
            L[f] = L2[f2]
            count = count+half-f1
            f2 = f2+1
        f = f+1
    return count


a =  [1,5,4,8,10,2,6,9,3,7]
print(SortCount(a))