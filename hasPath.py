graph = {
    'i': ['j', 'k'],
    'j': ['i', 'k'],
    'k': ['i', 'm', 'l',],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['0']
}

def undirectedPath(src, dest):
    return hasPath(graph, src, dest)

visited = set()

def hasPath(graph, src, dest):
    if src == dest:
        return True

    if src in visited:
        return False
    
    visited.add(src)
    print(src)
    
    neighbors = graph.get(src)
    
    for neighbor in neighbors:
        if hasPath(graph, neighbor, dest) == True:
            return True
            
    return False
    
print(undirectedPath('i', 'l'))