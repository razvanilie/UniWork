# Python program to deetect cycle in
# a directed graph

from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.noOfNodes = len(self.graph)

    def cycleRecursive(self, node, color):
        color[node] = 1

        for x in self.graph[node]:
            if color[x] == 1:
                return True
            elif color[x] == 0:
                if self.cycleRecursive(x, color) == True:
                    return True

        color[node] = 2
        return False

    def hasCycle(self):
        color = defaultdict(int)

        for i in range(self.noOfNodes):
            if color[i] == 0:
                if self.cycleRecursive(i, color) == True:
                    return True
        return False


# Driver program to test above functions

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


if g.hasCycle():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

# This program is contributed by Divyanshu Mehta