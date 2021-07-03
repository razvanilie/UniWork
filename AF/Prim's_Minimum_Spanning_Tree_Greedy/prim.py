from collections import defaultdict
import sys


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.noOfNodes = len(self.graph)
        self.mstSet = set()
        self.keyValues = defaultdict(lambda : sys.maxsize)
        self.parent = defaultdict(lambda: -1)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
        self.noOfNodes = len(self.graph)

    def printGraph(self):
        print(self.graph)
        print(self.noOfNodes)
        for x in self.mstSet:
            print(x)
        print("xxxx")

    def prim(self):
        self.mstSet.add(0)
        self.keyValues[0] = 0
        suma = 0
        self.parent[0] = -1 # it s already -1 from defaultdict
        self.graf = dict()
        for g in self.graph[0]:
                self.graf[g[0]] = (0, g[0], g[1])
                self.keyValues[g[0]] = g[1]
        while len(self.mstSet) != self.noOfNodes:
            tuplu = min(self.graf.items(), key=lambda x: x[1][2])
            print("tuplu", tuplu)
            self.mstSet.add(tuplu[0])
            self.graf.pop(tuplu[0])
            suma = suma + tuplu[1][2]
            for g in self.graph[tuplu[0]]:
                if g[0] not in self.mstSet and g[1] < self.keyValues[g[0]]:
                    self.graf[g[0]] = (tuplu[0], g[0], g[1])
                    self.keyValues[g[0]] = g[1]
        print("gata while")
        print(self.graf)
        print(self.mstSet)
        print(self.keyValues)
        #print(min(graf, key=lambda x: x[2]))
        print("suma", suma)


g = Graph()
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 8, 2)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

g.printGraph()
g.prim()
