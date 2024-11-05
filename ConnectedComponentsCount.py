graph = {
    'i': ['j', 'k'],
    'j': ['i', 'k'],
    'k': ['i', 'm', 'l',],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

visited = set()

def connectedComponentsCount():
    count = 0
    for node in graph:
        if node not in visited:
            explore(graph, node)
            count += 1
            
    return count
        
def explore(graph, node):
    if node in visited:
        return 
    
    print(node)
    visited.add(node)
    
    neighbors = graph.get(node)
    
    for neighbor in neighbors:
        explore(graph, neighbor)
            
print(connectedComponentsCount())
