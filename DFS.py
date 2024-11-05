graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':  [],
    'f':  [],
    'g': []
}

graph1 = {
    '1114': ['2114'],
    '2114': ['2505'],
    '2505': ['2506', '3114'],
    '2506': ['3214'],
    '3214': [],
    '3114': ['2506', '3604', '3304'],
    '3604': [],
    '3304': []
}

stack = []
ordering = []

def dfsRecursive(graph, startingPoint):
    # print(startingPoint)
    
    neighbors = graph.get(startingPoint)
    
    for neighbor in neighbors:
        dfsRecursive(graph, neighbor)
        
    if startingPoint not in ordering:
        ordering.insert(0, startingPoint)

def depthFirstTraversal(graph, startingPoint):
    stack.append(startingPoint)
    
    while len(stack) > 0:
        next = stack.pop()
        
        print(next)
        
        neighbors = graph.get(next)
        
        for neighbor in neighbors:
            stack.append(neighbor)
            
        
            

# depthFirstTraversal(graph, 'a')

stack = []
order = []
visited = []

def topologicalSort(graph, startingPoint):
    stack.append(startingPoint)
    
    while len(stack) > 0:
        curr = stack.pop()
        
        neighbors = graph.get(curr)
        
        for neighbor in neighbors:
            stack.append(neighbor)
            
        if curr not in visited:
            visited.append(curr)
            order.append(curr)
            
topologicalSort(graph1, '1114')
print(order)
#6XktiYLR8AXO8XyI