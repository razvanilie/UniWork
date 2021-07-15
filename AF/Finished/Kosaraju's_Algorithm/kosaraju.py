# For an undirected graph, it's easy since we can do a simple DFS search and if it goes through all the nodes than
# it is strongly connected
# For a directed graph
# create a stack, run a dfs and add the element to the stack after all its children have been visited
# reverse directions and do dfs for each element from stack

from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self, x, visited):
        print(x, end=",")
        visited[x] = True
        for node in self.graph[x]:
            if visited[node] == False:
                self.DFS(node, visited)

    def DFSwithStack(self, x, visited, stack):
        visited[x] = True
        for node in self.graph[x]:
            if visited[node] == False:
                self.DFSwithStack(node, visited, stack)
        stack.append(x)
    def printGraph(self):
        for x in self.graph:
            print(x, self.graph[x])

    def getTranspose(self):
        gT = Graph(self.V)
        for x in self.graph:
            for y in self.graph[x]:
                gT.addEdge(y, x)
        return gT

    def stronglyConnected(self):
        visited = [False for x in range(self.V)]
        stack = []
        for x in range(self.V):
            if visited[x] == False:
                self.DFSwithStack(x, visited, stack)
        #print(stack)

        gT = self.getTranspose()
        #gT.printGraph()
        visited = [False for x in range(self.V)]

        while len(stack) > 0:
            i = stack.pop()
            if visited[i] == False:
                gT.DFS(i, visited)
                print()



g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
#g.printGraph()
g.stronglyConnected()