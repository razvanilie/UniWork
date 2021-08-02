'''Se citesc informații despre un graf orientat fără circuite G din fișierul graf.in.
Fișierul are următoarea structură:
- Pe prima linie sunt două numere reprezentând numărul de vârfuri n (n>4) și numărul de arce
m ale grafului, m>=n
- Pe următoarele m linii sunt câte 3 numere întregi reprezentând extremitatea inițială,
extremitatea finală și costul unui arc din graf (costul unui arc poate fi și negativ).
- Pe ultima linie sunt două noduri sursa s1 și s2
a) Să se determine dacă există un vârf din graf v egal depărtat de s1 și s2: d(s1,v)=d(s2,v).
Dacă există mai multe astfel de vârfuri se va afișa cel mai apropiat de cele două surse
(cel cu d(s1,v) cea mai mică). Complexitate O(m)
b) Pentru vârful v determinat la a) (dacă există) să se determine dacă există mai multe
drumuri minime de la s1 la v. Daca exista doar unul, se va afișa acest drum, dacă nu se
vor afișa două dintre drumurile minime de la s la v1 Complexitate O(m)
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

        self.exista = True
        self.adj = defaultdict(list)

    def addEdge(self, u, v, w):
        self.matrix[u][v] = w
        self.adj[u].append(v)
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

    def vfegaldepartat(self, s1, s2):
        min_val = sys.maxsize
        nod = -1
        for x in range(len(self.matrix[0])):
            if self.matrix[s1][x] == self.matrix[s2][x]:
                if self.matrix[s1][x] < min_val:
                    min_val = self.matrix[s1][x]
                    nod = x
        if nod == -1:
            self.exista = False
        else:
            print("v = ", nod + 1)
            self.nodFinal = nod
            self.greutateFinala = min_val

    # Pt punctul b) de aici
    def punctb(self, s1):
        # build di-graph
        if self.exista == False:
            return []
        d = {}
        for i in range(self.vertixes):
            d[i] = self.adj[i]  # one-way link

        # apply DFS on DAG
        n = self.vertixes
        stack = [(s1, [s1])]  # - store noth the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == self.nodFinal:
                suma = 0
                for x in range(len(path) - 1):
                    suma += self.matrix[path[x]][path[x + 1]]
                if suma == self.greutateFinala:
                    path = list(map(lambda x: x + 1, path)) #add 1 to all elements
                    res.append(path)
            # traverse rest
            for x in d[node]:
                stack.append((x, path + [x]))
        return res


f = open('graf.in', 'r')
firstline = f.readline()
n = int(firstline.split()[0])
m = int(firstline.split()[1])
g = Graph(n)
for i in range(m):
    line = f.readline()
    g.addEdge(int(line.split()[0]) - 1, int(line.split()[1]) - 1, int(line.split()[2]))

line = f.readline()
s1 = int(line.split()[0]) - 1
s2 = int(line.split()[1]) - 1

g.printGraph()
g.floydWarshall()
g.printGraph()
print("a)")
g.vfegaldepartat(s1, s2)
print("b)")
t = 3
print(g.punctb(s1))
#g.longestPath(u, v)


