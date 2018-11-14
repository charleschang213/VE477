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
    a = sg.sparsegraph(7)
    for i in range(7):
        a.SetVertexValue(i,i)
    a.AddFlow(0,1,3);a.AddFlow(0,3,3)
    a.AddFlow(1,2,4)
    a.AddFlow(2,0,3);a.AddFlow(2,3,1);a.AddFlow(2,4,2)
    a.AddFlow(3,4,2);a.AddFlow(3,5,6)
    a.AddFlow(4,6,1);a.AddFlow(4,1,1)
    a.AddFlow(5,6,9)
    print(EK(a,0,6))

if __name__=='__main__':
    main()