from collections import defaultdict,deque
class Graph:
    def __init__(self,collections):
        self.collections = collections
        self.graph_dict = defaultdict(list)
        for vertex,edge in self.collections:
            self.graph_dict[vertex].append(edge)

    def bfs(self,start):
        que = deque()
        que.append(start)
        visited = set()
        path = []
        
        while que:
            vertex = que.popleft()
            
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                
                for neighbour in self.graph_dict[vertex]:
                    que.append(neighbour)
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
    # graph.display()
    print(graph.bfs("Mumbai"))