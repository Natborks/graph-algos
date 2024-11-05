from heapq import heappush, heappop

# A graph as an Adjacency list
class Node:
    def __init__(self, value, dist = float('inf')) -> None:
        self.value = value
        self.neighbors = []
        self.dist = dist
        self.parent = None
        
    def getNeighbors(self):
        return self.neighbors
    
    def getValue(self):
        return self.value
    
    def setValue(self, val):
        self.value = val
        
    def __eq__(self, value: object) -> bool:
        return self.value == value.value and self.neighbors == value.neighbors
    
    def __lt__(self, other):
        return self.dist < other.dist
    

class Graph:

    #Initialize a graph with n vertices
    def __init__(self, n) -> None:
        self.nodeArray = []
        self.edges = []
        
    def nodeCount(self):
        return len(self.nodeArray)
    
    def getNode(self, v):
        return self.nodeArray[v]
    
    def setNode(self, v, val):
        self.nodeArray[v] = val   
        
    def find(self, v):
        for node in self.nodeArray:
            if node == v:
                return node
            
        return None
    
    def getNodes(self):
        return self.nodeArray
        
    
    def addNode(self, node):
        self.nodeArray.append(node)
    
    def addEdge(self, v, node, weight = 0):
        curr = self.find(v)
        
        if v not in self.nodeArray:
            self.nodeArray.append(v)
            
        if node not in self.nodeArray:
            self.nodeArray.append(node)
        
        curr.neighbors.append([node, weight])
        node.neighbors.append([curr, weight])
        
    # def removeEdge(self, v, node):
    #     curr = self.find(v)
        
    #     curr.neighbors.remove(node)
    #     node.neighbors.remove(curr)

        
g = Graph(4)
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
h = Node('h')
g.addNode(a)
g.addNode(h)
g.addEdge(a, b)
g.addEdge(a, c)
g.addEdge(b, d)
g.addEdge(c, f)
g.addEdge(c, e)


def traverseGraph(graph):
    visited = []
    nodes = graph.getNodes()
    
    
    for node in nodes:
        if node not in visited:
            dfs(graph, node, visited)
    
def dfs(graph, startingPoint, visited):
    print(startingPoint.getValue())
    
    visited.append(startingPoint)
    
    neighbors = startingPoint.getNeighbors()
    
    for neighbor in neighbors:
        if neighbor[0] not in visited:
            dfs(graph, neighbor[0], visited)

import heapq



graph = {
    'S': {'B': 3, 'A': 1},
    'A': {'S' : 1, 'B': 2, 'C': 7},
    'B': {'A': 2, 'S': 3, 'C': 8},
    'C': {'A': 7, 'B': 8, 'D': 1, },
    'D': {'B': 8, 'C': 1},
}

def prims(graph, start_vertex):
    mst_edges = []
    visited = set()
    min_heap = []

    visited.add(start_vertex)
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(min_heap, (weight, start_vertex, neighbor))


    while min_heap:
        weight, from_node, to_node = heapq.heappop(min_heap)
        
        if to_node not in visited:
            visited.add(to_node)
            mst_edges.append((from_node, to_node, weight))
            
            for neighbor, edge_weight in graph[to_node].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, to_node, neighbor))
                    
 
    return mst_edges

mst_result = prims(graph, 'S')

for edge in mst_result:
    print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")
    
    
                

# shortestPath(g)

