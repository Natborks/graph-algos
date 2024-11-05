graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e':  [],
    'f':  []
}

queue = []

def breadthFirstTraversal(graph, startingPoint):
    queue.append(startingPoint)
    
    while len(queue) > 0:
        next = queue.pop(0)
        
        print(next)
        
        neighbors = graph.get(next)

        for neighbor in neighbors:
            queue.append(neighbor)
            

breadthFirstTraversal(graph, 'a')