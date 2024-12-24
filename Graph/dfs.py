from collections import deque
from collections import defaultdict
class Graph:
    def __init__(self,collection):
        self.collection = collection
        self.graph_dict = defaultdict(list)
        for vertex,edge in self.collection:
            self.graph_dict[vertex].append(edge)
    
    def dfs(self,start):
        stack = deque()
        visited = set()
        stack.append(start)
        path = []
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                
                for neighbour in self.graph_dict[vertex]:
                    stack.append(neighbour)       
                    
        return path

    
    def display(self):
        print(dict(self.graph_dict))
        
if __name__ == '__main__':
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New york"),
        ("Dubai","New york"),
        ("New york","Torrento"),
    ]
    graph = Graph(routes)
    graph.display()
    print(graph.dfs("Mumbai"))