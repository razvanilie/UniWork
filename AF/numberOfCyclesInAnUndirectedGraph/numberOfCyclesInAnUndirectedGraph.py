'''
We want to find if we have cycles in an undirected graph and if we have than we will print them
'''


from collections import defaultdict
# if we have this edges: (1,2),(2,3),(2,5),(3,4),(4,5) in an undirected graph
# the graphAsList variable will look like {1: [2], 2: [1, 3, 5], 3: [2, 4], 5: [2, 4], 4: [3, 5]}
graphAsListDict = defaultdict(list)

# addining edges
def addEdge(u, v):
    graphAsListDict[u].append(v)
    graphAsListDict[v].append(u)


# Made a DFS to traverse each node and its neighbours and if a node has been traversed but not all its
# neighbors have been traversed it means we went there once and now we have a cycle
def DFS(currentNode, parentNode):
    # it was traversed and completed
    if visited[currentNode] == 2:
        return

    # we have a cycle since it was traversed for a first time but was not completed
    # we will assign the parentNode to a new variable cycleNode
    # and with a while that stops when we are at the currentNode again we will print all the vertexes in the graph
    # if we have 1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 6], 5: [3, 6], 6: [4, 5]
    # the output will be 5 6 4 3 since now the parent for 3 sent via the function arguments is 5
    # the parent of 5 in parentList is 6, the parent of 6 in parentList is 4, the parent of 4 is 3
    # but the parent of 3(cycleNode) is equal to the parent of currentNode(3) so the while stops
    if visited[currentNode] == 1:
        cycleNode = parentNode
        while(cycleNode != parentList[currentNode]):
            print(cycleNode, end=" ")
            cycleNode = parentList[cycleNode]
        print()
        return


    parentList[currentNode] = parentNode
    # traversed but not completed
    visited[currentNode] = 1

    # go through neighbours
    # if we have 3: [2, 4, 5] with 2 being the parent of node 3 we will go only through 4 and 5
    # since 2 is the parent of 3
    # but if we have 1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 6], 5: [3, 6], 6: [4, 5]:
    # the parent of 4 is 3, the parent of 6 is 4, the parent of 5 is 6 but the parent of 3 is 2
    # so we will go from 5 to 3 and we'll find a cycle
    for eachNode in graphAsListDict[currentNode]:
        if eachNode != parentNode:
            DFS(eachNode, currentNode)

    # mark it as traversed and completed
    visited[currentNode] = 2

addEdge(1, 2)
addEdge(2, 3)
addEdge(3, 4)
addEdge(4, 6)
addEdge(4, 7)
addEdge(5, 6)
addEdge(3, 5)
addEdge(7, 8)
addEdge(6, 10)
addEdge(5, 9)
addEdge(11, 10)
addEdge(11, 12)
addEdge(11, 13)
addEdge(12, 13)
print(graphAsListDict)

parentList = defaultdict(int)
visited = defaultdict(int)
DFS(1, 0)

print(parentList)