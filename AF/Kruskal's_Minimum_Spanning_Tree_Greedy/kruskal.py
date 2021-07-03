from collections import defaultdict


def cycleRecursive(graph, node, visited, parent):
    visited[node] = True
    for x in graph[node]:
        if visited[x] == False:
            if (cycleRecursive(graph, x, visited, node) == True):
                return True
        # if it is visited but not parent then we have a cycle
        elif visited[x] == True:
            if parent != x:
                return True

    return False


def hasCycle(graph, noOfNodes):
    visited = defaultdict(bool)
    for i in range(noOfNodes):
        if visited[i] == False:
            if (cycleRecursive(graph, i, visited, -1)) == True:
                return True

    return False

class Graph:
    def __init__(self, n):
        self.graph = []
        self.noOfNodes = n

    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))


    def kruskal(self):
        # used a list for the graph and not a defaultdict cause i want to sort it and idk to sort a defaultdicts
        sortedGraph = sorted(self.graph, key=lambda item : item[2], reverse=False)
        print(sortedGraph)
        i = 0
        # we will use this to find if we have cycles
        dictGraph = defaultdict(list)
        noOfEdges = 0
        result = []

        #while we have vertexes to cover
        while noOfEdges < self.noOfNodes - 1:
            u, v, w = sortedGraph[i]
            i = i + 1
            dictGraph[u].append(v)
            dictGraph[v].append(u)
            lenOfDictGraph = len(dictGraph)
            print(dictGraph, hasCycle(dictGraph, lenOfDictGraph))
            if hasCycle(dictGraph, lenOfDictGraph) == False: #no cycle
                noOfEdges = noOfEdges + 1
                result.append([u, v, w])
            else: # if it has a cycle then jump over it and delete it from the pool
                dictGraph[u].remove(v)
                dictGraph[v].remove(u)

        print(result)
        minimumCost = 0
        for eachTuple in result:
            minimumCost = minimumCost + eachTuple[2]
        print("Minimum Cost Spanning Tree:", minimumCost)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskal()