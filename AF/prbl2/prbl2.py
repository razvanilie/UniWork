'''
Se citesc informații despre un graf orientat fără circuite G din fișierul graf.in.
Fișierul are următoarea structură:
- pe prima linie sunt două numere reprezentând numărul de vârfuri n (n>4) și numărul de arce
m ale grafului
- pe următoarele m linii sunt câte 3 numere întregi reprezentând extremitatea inițială,
extremitatea finală și costul unui arc din graf (costul unui arc poate fi și negativ).
- pe penultima linie sunt două noduri s și t
- pe ultima linie sunt două noduri u și v.
Spunem că un vârf y este accesibil din x în G dacă există un drum de la x la y. Presupunem că
vârful t este accesibil din s și că vârful v este accesibil din u.
a) Să se determine excentricitatea vârfului s raportat la t: ec(s|t) = max{d(s,t)+d(t,v)| v
accesibil din t}= d(s,t) + max{ d(t,v)| v accesibil din t}. Complexitate O(n+m)
b) Să se afișeze un drum de cost maxim de la u la v în G. Complexitate O(n+m)
cu topological sorting
'''
from collections import defaultdict
import sys
INF = sys.maxsize

class Graph:
    def __init__(self, n):
        self.vertixes = n
        self.matrix = [[INF for x in range(n)] for y in range(n)] # initialize with infinite first
        for x in range(n):
            self.matrix[x][x] = 0 # the distances on diagonal will be 0
        # now it looks something like this
        '''
        0 INF INF INF 
        INF 0 INF INF 
        INF INF 0 INF 
        INF INF INF 0 
        '''

        self.adj = defaultdict(list)
        self.st = []
        self.visited = defaultdict(bool)

    def addEdge(self, u, v, w):
        self.matrix[u][v] = w
        self.adj[u].append([v,w])
        '''
        g5.addEdge(0, 1, 5)
        g5.addEdge(0, 3, 10)
        g5.addEdge(1, 2, 3)
        g5.addEdge(2, 3, 1)
        '''
        # after the last addition the matrix will look something like this
        '''
        0 5 INF 10
        INF 0 3 INF
        INF INF 0 1
        INF INF INF 0
        '''

    def printGraph(self):
        print('\n')
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == sys.maxsize:
                    print("INF", end=" | ") # it s ugly to show 9223372036854775807, better INF
                else:
                    print(self.matrix[i][j], end=" | ") # if it's not the ugly maxint then print it
            print()

    def floydWarshall(self):
        for k in range(self.vertixes):
            # pick all vertices as source one by one
            for i in range(self.vertixes):
                # Pick all vertices as destination for the
                # above picked source
                for j in range(self.vertixes):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    if not(self.matrix[i][k] == sys.maxsize or self.matrix[k][j] == sys.maxsize):
                        self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])

    def excentricitate(self, s, t):
        print("d(s,t) = ", end="")
        print(self.matrix[s][t])
        print("Varfuri accesibile din t: ", end="")
        for x in range(len(self.matrix[t])):
            if self.matrix[t][x] != sys.maxsize:
                print(x + 1, end=" ")

        print("\nCea mai mare distanta: ", end="")
        max = 0
        for x in range(len(self.matrix[t])):
            if self.matrix[t][x] != sys.maxsize:
                if self.matrix[t][x] > max:
                    max = self.matrix[t][x]
        print(max)

# Pt punctul b) de aici
    def topologicalSortUtil(self, v):
        self.visited[v] = True

        for i in self.adj[v]:
            if self.visited[i[0]] == False:
                self.topologicalSortUtil(i[0])

        self.st.append(v)

    def longestPath(self, start, end):
        dist = [-sys.maxsize for i in range(self.vertixes)]

        for i in range(self.vertixes):
            if self.visited[i] == False:
                self.topologicalSortUtil(i)

        dist[start] = 0

        while len(self.st) > 0:
            u = self.st.pop(-1)

            for i in self.adj[u]:
                if dist[i[0]] < (dist[u] + i[1]):
                    dist[i[0]] = dist[u] + i[1]

        print(dist)
        print("Distanta maxima de la u la v este", dist[v])


f = open('graf.in', 'r')
firstline = f.readline()
n = int(firstline.split()[0])
m = int(firstline.split()[1])
g = Graph(n)
for i in range(m):
    line = f.readline()
    g.addEdge(int(line.split()[0]) - 1, int(line.split()[1]) - 1, int(line.split()[2]))

line = f.readline()
s = int(line.split()[0]) - 1
t = int(line.split()[1]) - 1
line = f.readline()
u = int(line.split()[0]) - 1
v = int(line.split()[1]) - 1

g.printGraph()
g.floydWarshall()
g.printGraph()
print("a)")
g.excentricitate(s, t)
print("b)")

g.longestPath(u, v)
