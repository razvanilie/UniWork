
from collections import defaultdict
import sys
class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.id = 0
        self.ap = set()

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def AP(self, x, visited, parent, low, disc):
        low[x] = self.id
        disc[x] = self.id #discovery time
        self.id += 1
        children = 0
        visited[x] = True
        for node in self.graph[x]:
            if visited[node] == False: #not visited
                parent[node] = x
                children += 1
                self.AP(node, visited, parent, low, disc)
                low[x] = min(low[x], low[node]) # like tarjan
                # if x is the root and has at least 2 children
                if parent[x] == -1 and children >= 2:
                    self.ap.add(x)
                # if u is not the root and low value is more than discovery value
                elif parent[x] != -1 and low[node] >= disc[x]:
                    self.ap.add(x)
            elif node != parent[x]: #it's in stack so is not a crossedge
                low[x] = min(low[x], disc[node])

    def printGraph(self):
        for x in self.graph:
            print(x, self.graph[x])

    def articulationPoints(self):
        visited = [False for x in range(self.V)]
        disc = [sys.maxsize for x in range(self.V)]
        low = [sys.maxsize for x in range(self.V)]
        parent = [-1 for x in range(self.V)]
        for x in range(self.V):
            if visited[x] == False:
                self.AP(x, visited, parent, low, disc)
        #print(stack)
        for x in self.ap:
            print(x)





g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
#g.printGraph()
g.articulationPoints()