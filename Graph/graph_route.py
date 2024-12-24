from collections import deque
class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for vertex, edge in self.edges:
            if vertex in self.graph_dict:
                self.graph_dict[vertex].append(edge)
            else:
                self.graph_dict[vertex] = [edge]
    
    def find_path(self, start, end, path = []):
        path = path + [start]
        
        if start not in self.graph_dict:
            return []
        
        if start == end:
            return [path]
        
        paths = []
        for node in self.graph_dict[start]:
            if node in self.graph_dict:
                new_path = self.find_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        
        return paths
    
    # def get_shortest_path(self,start,end,path=[]):
        # path = path + [start]
        
        # if start not in self.graph_dict:
        #     return None
        
        # if start == end :
        #     return path
        
        # shortest_path = None
        # for node in self.graph_dict[start]:
        #     if node in self.graph_dict:
        #         sp = self.get_shortest_path(node,end,path)
        #         if sp:
        #             if shortest_path is None or len(sp) < len(shortest_path):
        #                 shortest_path = sp
                        
        # return shortest_path
    
    def get_shortest_path(self,start,end):
        que = deque([(start,[start])])
        
        while que:
            current, path = que.popleft()
            
            if current == end:
                return path
            
            for neighbour in self.graph_dict[current]:
                if neighbour not in path:
                    que.append((neighbour, path + [neighbour]))
        return None
    
    def display(self):
        print('graph : ',self.graph_dict)

if __name__ == '__main__':
    routes = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New york"),
        ("Dubai","New york"),
        ("New york","Torrento"),
    ]
    route_graph = Graph(routes)
    route_graph.display()
    
    start = "Mumbai"
    end = "New york"
    
    print(f'paths starting from {start} and ending at {end} : ',route_graph.find_path(start,end))
    print(f'shortest path starting from {start} and ending at {end} : ',route_graph.get_shortest_path(start,end))