
from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.id = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSwithStack(self, x, low, disc, vertexesInStack, stack):
        low[x] = self.id
        disc[x] = self.id
        self.id += 1
        vertexesInStack[x] = True
        stack.append(x)
        for node in self.graph[x]:
            if disc[node] == -1: #not visited
                self.DFSwithStack(node, low, disc, vertexesInStack, stack)
                low[x] = min(low[x], low[node])
            elif vertexesInStack[node] == True: #it's in stack so is not a crossedge
                low[x] = min(low[x], low[node])
        w = -1  # To store stack extracted vertices
        if low[x] == disc[x]:
            while w != x:
                w = stack.pop()
                print(w, end=",")
                vertexesInStack[w] = False

            print()

    def printGraph(self):
        for x in self.graph:
            print(x, self.graph[x])

    def stronglyConnected(self):
        vertexesInStack = [False for x in range(self.V)]
        disc = [-1 for x in range(self.V)]
        low = [-1 for x in range(self.V)]
        stack = []
        for x in range(self.V):
            if disc[x] == -1:   #it's pretty much the same as visited
                self.DFSwithStack(x, low, disc, vertexesInStack, stack)
        #print(stack)





g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
#g.printGraph()
g.stronglyConnected()