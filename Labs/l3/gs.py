def GaleShapley(m,w):
    n = len(m)
    freeman = [1 for i in range(n)]
    propose = [0 for i in range(n)]
    pairedwoman = [-1 for i in range(n)]
    while (sum(freeman)!=0):
        nowman = freeman.index(1)
        target = m[nowman][propose[nowman]]
        propose[nowman] = propose[nowman]+1 
        if (pairedwoman[target]==-1):
            pairedwoman[target]=nowman
            freeman[nowman]=0
        else:
            rival = pairedwoman[target]
            if (w[target].index(nowman)<w[target].index(rival)):
                pairedwoman[target] = nowman
                freeman[nowman]=0
                freeman[rival]=1
    result = []
    for i in range(n):
        result.append((pairedwoman[i],i))
    return result
        

woman = [[2,1,0,3],[3,0,1,2],[2,3,0,1],[0,1,2,3]]
man =  [[0,1,2,3],[0,3,2,1],[0,2,3,1],[0,2,1,3]]
print(GaleShapley(man,woman))
