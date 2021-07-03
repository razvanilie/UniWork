from collections import defaultdict
def addEdge(u, v):
    graph[u].append(v)
    # graph[v].append(u) # it depends if it s a directed or undirected graph

#BFS starting with node x
def BFS(x):
    visitedArray[x] = True
    queueAsList = []
    queueAsList.append(x)
    while queueAsList:
        currentNode = queueAsList[0]
        print(currentNode)
        queueAsList.pop(0)
        for y in graph[currentNode]:
            if(visitedArray[y] == False):
                visitedArray[y] = True
                queueAsList.append(y)


numberOfNodes = 6 #number of vertexes
visitedArray = [False for x in range(numberOfNodes)] #initialise an array of numberOfNodes length with false values
# graph = [[] for x in range(numberOfNodes)] # for each node we will append the nodes with a common edge
graph = defaultdict(list)
print(visitedArray)
# print(graph)

addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 2)
addEdge(2, 0)
addEdge(2, 3)
addEdge(3, 3)
print("After we added the edges\n" + str(graph))
BFS(2)