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

    def addEdge(self, u, v, w):
        self.matrix[u][v] = w
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
                    self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])


g5 = Graph(4)
g5.addEdge(0, 1, 5)
g5.addEdge(0, 3, 10)
g5.addEdge(1, 2, 3)
g5.addEdge(2, 3, 1)
g5.printGraph()
g5.floydWarshall()
g5.printGraph()
