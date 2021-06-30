#http://www.cs.yale.edu/homes/aspnes/pinewiki/DepthFirstSearch.html

from collections import defaultdict
def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u) # it depends if it s a directed or undirected graph

#DFS starting with node x
def DFS(x):
    visitedArray[x] = True
    print(x)
    for y in graph[x]:
        if(visitedArray[y] == False):
            DFS(y)


numberOfNodes = 6 #number of vertexes
visitedArray = [False for x in range(numberOfNodes)] #initialise an array of numberOfNodes length with false values
# graph = [[] for x in range(numberOfNodes)] # for each node we will append the nodes with a common edge
graph = defaultdict(list)
print(visitedArray)
# print(graph)

addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(1, 2)
addEdge(2, 3)
addEdge(3, 4)
addEdge(4, 1)
addEdge(4, 0)
addEdge(4, 5)
print("After we added the edges\n" + str(graph))
DFS(0)