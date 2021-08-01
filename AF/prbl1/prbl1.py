# Se dă un graf neorientat conex cu n>3 vârfuri și m>n muchii.
# Informațiile despre graf se citesc din fișierul graf.in cu următoarea structură:
# - pe prima linie sunt n și m
# - pe următoarele m linii sunt câte 2 numere naturale reprezentând extremitățile unei
# muchii
# Se citește de la tastatură un vârf v.
# a) Să se afișeze muchiile critice care sunt incidente în v, dacă există (altfel se va afișa mesajul
# “nu exista”). O(m)
# b) Să se afișeze listele de adiacență ale unui arbore parțial T al lui G în care vârful v are
# gradul cu 1 mai mic decât îl are în G: dT(v) = dG(v) – 1, dacă un astfel de arbore există O(m)

from collections import defaultdict
import sys
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.id = 0
        self.muchii_incidente_in_v = 0
        self.visitedArray = [False for x in range(V)]
        self.tree = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for x in self.graph:
            print(x, self.graph[x])

    def bridgeUtil(self, x, visited, parent, low, disc):

        # Mark the current node as visited and print it
        visited[x] = True

        # Initialize discovery time and low value
        disc[x] = self.id
        low[x] = self.id
        self.id += 1

        # Recur for all the vertices adjacent to this vertex
        for node in self.graph[x]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[node] == False:
                parent[node] = x
                self.bridgeUtil(node, visited, parent, low, disc)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[x] = min(low[x], low[node])

                if low[node] > disc[x]:
                    if x == self.v or node == self.v:
                        print(x + 1, node + 1)
                        self.muchii_incidente_in_v += 1


            elif node != parent[x]:  # Update low value of u for parent function calls
                low[x] = min(low[x], disc[node])

    # DFS based function to find all bridges. It uses recursive
    # function bridgeUtil()
    def bridge(self, v):
        self.v = v
        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False for x in range(self.V)]
        disc = [sys.maxsize for x in range(self.V)]
        low = [sys.maxsize for x in range(self.V)]
        parent = [-1 for x in range(self.V)]

        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        self.bridgeUtil(v, visited, parent, low, disc)

        if self.muchii_incidente_in_v == 0:
            print("nu exista")

    def BFS(self, x):
        self.visitedArray[x] = True
        queueAsList = []
        queueAsList.append((x,x))
        while queueAsList:
            currentNode = queueAsList[0][1]
            if queueAsList[0][0] + 1 != currentNode + 1:
                self.tree[queueAsList[0][0] + 1].append(currentNode + 1)
                self.tree[currentNode + 1].append(queueAsList[0][0] + 1)
            #print(queueAsList[0][0] + 1, currentNode + 1)
            queueAsList.pop(0)
            for y in self.graph[currentNode]:
                if (self.visitedArray[y] == False):
                    self.visitedArray[y] = True
                    queueAsList.append((currentNode, y))

        for x in range(1, len(self.tree) + 1):
            print(x, end=": ")
            for y in self.tree[x]:
                print(y, end=" ")
            print()

    def arborepartial(self, v):

        for x in self.graph[v]:
            if len(self.graph[x]) >= 2:
                self.graph[v].remove(x)
                self.graph[x].remove(v)
                break
        print("Arbore:")
        self.BFS(v)



f = open('graf.in', 'r')
firstline = f.readline()
n = int(firstline.split()[0])
m = int(firstline.split()[1])
g = Graph(n)
for i in range(m):
    line = f.readline()
    g.addEdge(int(line.split()[0]) - 1, int(line.split()[1]) - 1)

#g.printGraph()
print("Enter v:")
v = int(input())
print("muchii critice:")
g.bridge(v - 1)

g.arborepartial(v - 1)
#g.prim()