import sparsegraph as sg

def EK(G,s,t):
    flow = 0
    n = G.vertex
    f = [[0 for i in range(n)] for i in range(n)]
    while True:
        Q = []
        Q.append(s)
        parent = [-1 for i in range(n)]
        while len(Q)!=0:
            v = Q[0]
            Q.remove(v)
            for i in G.edge[v]:
                if parent[i]==-1 and i!=s and G.GetEdgeWeight(v,i)>f[v][i]:
                    parent[i] = v
                    Q.append(i)
        if parent[t]!=-1:
            df = float("inf")
            e = parent[t]
            d = t
            while e!=-1:
                df = min(df,G.GetEdgeWeight(e,d)-f[e][d])
                d = e
                e = parent[e]
            e = parent[t]
            d = t
            while e!=-1:
                #print('Node',e)
                f[e][d] = f[e][d]+df
                f[d][e] = f[d][e]-df
                d = e
                e = parent[e]
            #print(df)
            flow = flow+df
        else:
            break
    return flow




def main():
    a = sg.sparsegraph(6)
    a.AddFlow(0,1,10);a.AddFlow(0,3,10)
    a.AddFlow(1,2,9)
    a.AddFlow(2,4,6);a.AddFlow(2,5,10)
    a.AddFlow(3,1,2);a.AddFlow(3,2,8);a.AddFlow(3,4,4)
    a.AddFlow(4,5,10)
    print(EK(a,0,5))

if __name__=='__main__':
    main()