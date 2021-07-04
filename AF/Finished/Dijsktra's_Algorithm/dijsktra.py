from collections import defaultdict
import sys # for int_max


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.mstSet = set() # here we will store all vertexes that are already in the mst
        self.keyValues = defaultdict(lambda : sys.maxsize) # minimum weight of each vertex

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])


    def prim(self):
        # print(self.graph)
        noOfNodes = len(self.graph)

        # add node 0
        self.mstSet.add(0)
        self.keyValues[0] = 0
        # suma = 0
        graf = dict()
        for g in self.graph[0]:
                graf[g[0]] = [0, g[0], g[1]]
                self.keyValues[g[0]] = g[1]

        #####

        # until we covered all vertexes
        while len(self.mstSet) != noOfNodes:
            # print("Keyvalues", self.keyValues)
            # get the node that has the minimum weight and is not in mst
            # more specifically the node that will be added in mst
            # print("Inainte de min: ", graf.items())
            nodeTuple = min(graf.items(), key=lambda x: x[1][2])
            nodeTuple = list(nodeTuple)
            print(nodeTuple[0], "Distance from source ", nodeTuple[1][2])

            self.mstSet.add(nodeTuple[0])
            # if we covered it then remove it from the pool of vertexes
            graf.pop(nodeTuple[0])

            # suma = suma + nodeTuple[1][2]
            # for every node (that is connected to the node with minimum weight)
            for g in self.graph[nodeTuple[0]]:
                #print("Pt nodul " + str(nodeTuple[0]) + " avem vecinul " + str(g) + " si mstset " + str(self.mstSet))
                # if it is not in the already covered nodes and the weight is smaller
                if g[0] not in self.mstSet and g[1] + self.keyValues[nodeTuple[0]] < self.keyValues[g[0]]:
                    # update the node in the pool
                    graf[g[0]] = [nodeTuple[0], g[0], g[1] + self.keyValues[nodeTuple[0]]]
                    self.keyValues[g[0]] = g[1] + self.keyValues[nodeTuple[0]]


        # print("mst sum", suma)


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

g.prim()
