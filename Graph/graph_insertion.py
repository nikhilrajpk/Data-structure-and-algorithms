class Graph:
    def __init__(self):
        self.map = {}
        
    def addVertex(self,key):
        self.map[key] = []
    
    def insert(self,vertex, edge, isBidirectional):
        if vertex not in self.map:
            self.addVertex(vertex)
        if edge not in self.map:
            self.addVertex(edge)
        
        self.map[vertex].append(edge)
        if isBidirectional:
            self.map[edge].append(vertex)
        
    def display(self):
        print(self.map)
if __name__ == '__main__':
    graph = Graph()
    graph.insert('nikhil','midhun',True)
    graph.insert('nikhil','vaishnav',True)
    graph.insert('midhun','nived',False)
    graph.display()