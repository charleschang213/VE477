import sparsegraph as sg

def bfs(G,s):
    n = G.vertex
    dist = [float("inf") for i in range(n)]
    parent = [-1 for i in range(n)]
    Q = []
    Q.append(s)
    dist[s] = 0
    while len(Q)!=0:
        v = Q[0]
        if v==s:
            print('Visit node',v,'with value',G.GetVertexValue(v),'as starting node')
        else:
            print('Visit node',v,'with value',G.GetVertexValue(v),'from node',parent[v])
        Q.remove(v)
        for i in G.edge[v]:
            if dist[i] == float("inf"):
                dist[i] = dist[v]+1
                parent[i] = v
                Q.append(i)
    


def main():
    a = sg.sparsegraph(8)
    for i in range(8):
        a.SetVertexValue(i,i)
    a.AddEdge(0,1,3);a.AddEdge(0,2,5);a.AddEdge(0,4,6)
    a.AddEdge(1,3,9);a.AddEdge(1,5,2);a.AddEdge(1,6,7)
    a.AddEdge(2,5,9);a.AddEdge(2,4,3);a.AddEdge(2,6,8)
    a.AddEdge(3,6,9);a.AddEdge(3,5,5)
    a.AddEdge(4,6,4);a.AddEdge(4,7,2)
    a.AddEdge(5,6,2);a.AddEdge(5,7,2)
    a.AddEdge(6,7,1)
    bfs(a,0)

if __name__ == '__main__':
    main()