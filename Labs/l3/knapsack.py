import timeit
import numpy as np
import matplotlib.pyplot as plt

def knapsack_small(S,n):
    if (n>sum(S)):
        return None
    S.sort()
    i = 1
    while (sum(S[0:i])<n):
        i = i+1
    if (sum(S[0:i])>n):
        return None
    return S[0:i]


def knapsack_big(S,n):
    if (n>sum(S)):
        return None
    S.sort()
    i = len(S)-1
    while (sum(S[i:])<n):
        i = i-1
    if (sum(S[i:])>n):
        return None
    return S[i:]

def knapsack_true(S,n):
    if (n>sum(S)):
        return None
    weights = [[]]
    weights = weights+([None for i in range(n)])
    for i in range(len(S)):
        have = []
        for j in range(n-S[i]+1):
            if not (weights[j] is None) and (weights[j+S[i]] is None) and not (j in have):
                weights[j+S[i]] = weights[j]+[S[i]]
                have.append(j+S[i])
    return weights[n]

print(knapsack_small([5,7,4,3,10,8,1,9,2,6],15))
print(knapsack_small([5,7,4,3,10,8,1,9,2,6],16))
print(knapsack_big([5,7,4,3,10,8,1,9,2,6],27))
print(knapsack_big([5,7,4,3,10,8,1,9,2,6],37))
print(knapsack_true([5,7,4,3,10,8,1,9,2,6],16))
print(knapsack_true([5,7,4,3,10,8,1,9,2,6],37))
timetrue = []
timesmall = []
timebig = []
input()
for i in range(100):
    print(i+1,"%")
    S = [j+1 for j in range(i)]
    n = int(sum(S)/2)
    timetrue.append(timeit.timeit("knapsack_true(S,n)","from __main__ import knapsack_true,S,n",number=50))
    timesmall.append(timeit.timeit("knapsack_small(S,n)","from __main__ import knapsack_small,S,n",number=50))
    timebig.append(timeit.timeit("knapsack_big(S,n)","from __main__ import knapsack_big,S,n",number=50))

plt.figure(1)
plt.plot(np.linspace(0,99,100),np.array(timetrue),label="Correct Algorithm")
plt.plot(np.linspace(0,99,100),np.array(timesmall),label="Small-First Algorithm")
plt.plot(np.linspace(0,99,100),np.array(timebig),label="Big-First Algorithm",ls='-.')
plt.xlabel("Size of S")
plt.ylabel("time(s)")
plt.legend()
plt.show()
