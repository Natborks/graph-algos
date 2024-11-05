# A graph as an Adjacency list
class Graph:
    
    #Doubly linked list node
    class Edge:
        def __init__(self, vertex, weight, prev, next) -> None:
            self.vertext = vertex
            self.weight = weight
            self.prev = prev
            self.next = next

    #Initialize a graph with n vertices
    def __init__(self, n) -> None:
        self.nodeArray = [self.Edge] * n
        
        for i in range(4):
            self.nodeArray[i] = self.Edge(-1, -1, None, None)
            
        self.nodeValues = [object] * n
        self.numEdge = 0
        
    def nodeCount(self):
        return len(self.nodeArray)
    
    def edgeCount(self):
        return self.numEdge
    
    def getValue(self, v):
        return self.nodeValues[v]
    
    def setValue(self, v, val):
        self.nodeValues[v] = val   
        
    #Return the link in v's neighbor list that preceeds the
    #one with w (or where it would be)
    def __find(self, v,  w):
        curr = self.nodeArray[v]
        while(curr.next != None and curr.next.vertext != w):
            curr = curr.next
        
        return curr
    
    def addEdge(self, v, w, wgt):
        if wgt == 0:
            return 
        curr = self.__find(v, w)
        
        if curr.next != None and curr.next.vertex == w:
            curr.next.weight = wgt
        else:
            curr.next = self.Edge(w, wgt, curr, curr.next)
            self.numEdge += 1
            if curr.next.next != None:
                curr.next.next.prev = curr.next
                
    def weight(self, v, w):
        curr = self.__find(v, w)
        if curr.next == None or curr.next.vertex != w:
            return 0
        else:
            return curr.next.weight 
        
    def removeEdge(self, v, w):
        curr = self.find(v, w)
        if (curr.next == None) or curr.next.vertext != w:
            return
        else:
            curr.next = curr.next.next
            if curr.next != None:
                curr.next.prev = curr
        
        
g = Graph(4)
print(g.nodeCount())
print(g.getValue(2))
