import sparsegraph as sg
import EK

class Bipartite:
    left = 0
    right = 0
    adj = []
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.adj = [[False for i in range(right)] for i in range(left)]
    def addEdge(self,left,right):
        self.adj[left][right]=True
    def MaxMatch(self):
        a = sg.sparsegraph(self.left+self.right+2)
        for i in range(self.left):
            a.AddFlow(0,i+1,1)
        for i in range(self.right):
            a.AddFlow(self.left+i+1,self.left+self.right+1,1)
        for i in range(self.left):
            for j in range(self.right):
                if self.adj[i][j]==True:
                    a.AddFlow(i+1,self.left+j+1,1)
        return EK.EK(a,0,self.left+self.right+1)

def main():
    G = Bipartite(5,4)
    G.addEdge(0,0)
    G.addEdge(1,0);G.addEdge(1,2)
    G.addEdge(2,1);G.addEdge(2,2);G.addEdge(2,3)
    G.addEdge(3,2)
    G.addEdge(4,2);G.addEdge(4,3)
    print(G.MaxMatch())

if __name__=='__main__':
    main()