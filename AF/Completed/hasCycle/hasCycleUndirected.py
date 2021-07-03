# Python Program to detect cycle in an undirected graph
# from geeksforgeeks
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
        self.noOfNodes = len(self.graph)


    def cycleRecursive(self, node, visited, parent):
        visited[node] = True
        for x in self.graph[node]:
            if visited[x] == False:
                if (self.cycleRecursive(x, visited, node) == True):
                    return True
            #if it is visited but not parent then we have a cycle
            elif visited[x] == True:
                if parent != x:
                    return True

        return False

    def hasCycle(self):
        visited = defaultdict(bool)
        for i in range(self.noOfNodes):
            if visited[i] == False:
                if (self.cycleRecursive(i, visited, -1)) == True:
                    return True

        return False


g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(0, 2)

if g1.hasCycle():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

# This code is contributed by Neelam Yadav
# modified by me
