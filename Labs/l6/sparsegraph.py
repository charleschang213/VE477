import fibheap as fh

class sparsegraph:
    vertex = 0
    edge = []
    weight = []
    vers = []
    def __init__(self,size):
        self.vertex = 0
        self.edge = []
        self.weight = []
        self.vers = []
        self.vertex = size
        self.weight = [([0]*size) for i in range(size)]
        for i in range(size):
            self.edge.append([])
        self.vers = [0]*size
    def RemoveEdge(self,s,t,directed=False):
        self.weight[s][t] = 0
        self.edge[s].remove(t)
        if directed==False:
            self.weight[t][s] = 0
            self.edge[t].remove(s)
    def AddFlow(self,s,t,w):
        self.edge[s].append(t)
        self.edge[t].append(s)
        self.weight[s][t]=w
    def AddEdge(self,s,t,w,directed=False):
        self.edge[s].append(t)
        self.weight[s][t] = w
        if directed==False:
            self.edge[t].append(s)
            self.weight[t][s] = w
    def AddVertex(self,w=0):
        self.edge.append([])
        self.vertex = self.vertex+1
        self.vers = self.vers+[w]
    def RemoveVertex(self,v):
        self.weight = list(map(lambda x:x[0:v]+x[v+1:],self.edge))
        self.weight = self.edge[0:v]+self.edge[v+1:]
        for i in range(self.vertex):
            try:
                self.edge[i].remove(v)
            except ValueError:
                pass
            for j in range(len(self.edge[i])):
                if self.edge[i][j]>v:
                    self.edge[i][j] = self.edge[i][j]-1
        self.vers = self.vers[0:v]+self.vers[v+1,:]
        self.vertex = self.vertex-1
    def IsAdjacent(self,s,t):
        try:
            self.edge[s].index(t)
        except ValueError:
            return False
        else:
            return True
    def GetEdgeWeight(self,s,t):
        return self.weight[s][t]
    def SetEdgeWeight(self,s,t,w,directed = False):
        self.weight[s][t] = w
        if directed==False:
            self.weight[t][s] = w
    def GetVertexValue(self,v):
        return self.vers[v]
    def SetVertexValue(self,v,w):
        self.vers[v] = w
    def BF(self,s,t):
        dist = [float("inf")]*self.vertex
        pre = [-1]*self.vertex
        dist[s] = 0
        for i in range(self.vertex-1):
            for j in range(self.vertex):
                for k in self.edge[j]:
                    tmp = dist[j]+self.GetEdgeWeight(j,k)
                    if tmp < dist[k]:
                        dist[k] = tmp
                        pre[k] = j
        print("The shortest length is",dist[t])
        flag = t
        ans = []
        while flag!=-1:
            ans.append(self.GetVertexValue(flag))
            flag = pre[flag]
        return ans
    def Dijkstra(self,s,t):
        dist = [float("inf")]*self.vertex
        pre = [-1]*self.vertex
        out = [False]*self.vertex
        pq = fh.Fibheap(0,0)
        dist[s] = 0
        pointers = [0]*10
        for i in range(self.vertex):
            pointers[i] = fh.Node(dist[i],i)
            pq.Insert(pointers[i])            
        v = s
        out[s] = True
        while v!=t:
            for u in self.edge[v]:
                tmp = dist[v]+self.GetEdgeWeight(v,u)
                if tmp < dist[u]:
                    dist[u] = tmp
                    pre[u] = v
                    if out[u]==False:
                        pq.DecreaseKey(pointers[u],dist[u])
            pq.Delete(pointers[v])
            v = pq.Minimum().value
            out[v]=True
        print("The shortest length is",dist[t])
        flag = t
        ans = []
        while flag!=-1:
            ans.append(self.GetVertexValue(flag))
            flag = pre[flag]
        return ans
                        
def main():
    a = sparsegraph(8)
    for i in range(8):
        a.SetVertexValue(i,i)
    a.AddEdge(0,1,3);a.AddEdge(0,2,5);a.AddEdge(0,4,6)
    a.AddEdge(1,3,9);a.AddEdge(1,5,2);a.AddEdge(1,6,7)
    a.AddEdge(2,5,9);a.AddEdge(2,4,3);a.AddEdge(2,6,8)
    a.AddEdge(3,6,9);a.AddEdge(3,5,5)
    a.AddEdge(4,6,4);a.AddEdge(4,7,2)
    a.AddEdge(5,6,2);a.AddEdge(5,7,2)
    a.AddEdge(6,7,1)
    b = sparsegraph(6)
    b.SetVertexValue(0,'s')
    b.SetVertexValue(1,'b')
    b.SetVertexValue(2,'c')
    b.SetVertexValue(3,'d')
    b.SetVertexValue(4,'e')
    b.SetVertexValue(5,'t')
    b.AddEdge(0,1,4,True);b.AddEdge(0,2,2,True)
    b.AddEdge(1,3,5,True)
    b.AddEdge(2,3,-3,True);b.AddEdge(2,4,10,True);b.AddEdge(2,5,8,True)
    b.AddEdge(3,4,2,True);b.AddEdge(3,5,-1,True)
    b.AddEdge(4,5,3,True)
    print("Dijkstra")
    print(a.Dijkstra(0,7))
    print("Bellman-Ford")
    print(b.BF(0,5))

if __name__ == '__main__':
    main()