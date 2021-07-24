# Python program to find bridges in a given undirected graph
# Complexity : O(V+E)

from collections import defaultdict
import sys

# This class represents an undirected graph using adjacency list representation
class Graph:

    def __init__(self, V):
        self.V = V  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.id = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

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
                    print("%d %d" % (x, node))


            elif node != parent[x]:  # Update low value of u for parent function calls
                low[x] = min(low[x], disc[node])

    # DFS based function to find all bridges. It uses recursive
    # function bridgeUtil()
    def bridge(self):

        # Mark all the vertices as not visited and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False for x in range(self.V)]
        disc = [sys.maxsize for x in range(self.V)]
        low = [sys.maxsize for x in range(self.V)]
        parent = [-1 for x in range(self.V)]

        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        for x in range(self.V):
            if visited[x] == False:
                self.bridgeUtil(x, visited, parent, low, disc)


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("Bridges")
g1.bridge()

# This code is contributed by Neelam Yadav
