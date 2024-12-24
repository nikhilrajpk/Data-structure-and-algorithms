# from collections import defaultdict, deque
# class Graph:
#     def __init__(self,routes):
#         self.routes = routes
#         self.graph_dict = defaultdict(list)
#         for vertex, edge in self.routes:
#             self.graph_dict[vertex].append(edge)
#     def display(self):
#         print(dict(self.graph_dict))
    
#     def get_path(self,start,end,path=[]):
#         path = path + [start]
        
#         if start not in self.graph_dict:
#             return []
        
#         if start == end:
#             return [path]
        
#         paths = []
#         for neighbour in self.graph_dict[start]:
#             if neighbour in self.graph_dict:
#                 new_path = self.get_path(neighbour,end,path)
#                 for i in new_path:
#                     paths.append(i)
#         return paths
    
#     def get_shortest_path(self,start,end,path=[]):
#         que = deque([(start,[start])])
        
#         while que:
#             current, path = que.popleft()
#             if current == end:
#                 return path
#             for neighbour in self.graph_dict[current]:
#                 if neighbour not in path:
#                     que.append((neighbour, path+[neighbour]))
                    
#     def bfs(self,start):
#         q = deque([start])
#         path = []
#         visited = set()
#         while q:
#             current = q.popleft()
#             if current not in visited:
#                 visited.add(current)
#                 path.append(current)
                
#                 for neighbour in self.graph_dict[current]:
#                     q.append(neighbour)
#         return path
        
# if __name__ == '__main__':
#     routes = [
#         ('Mumbai','Paris'),
#         ('Mumbai','Dubai'),
#         ('Paris','Dubai'),
#         ('Paris','New york'),
#         ('Dubai','New york'),
#         ('New york','Torrento'),
#     ]
#     graph = Graph(routes)
#     # graph.display()
    
#     start = "Mumbai"
#     end = "New york"
#     # print(graph.get_path(start,end))
#     # print(graph.get_shortest_path(start,end))
#     print(graph.bfs(start))


# class RiverSize:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.stack = []
#         self.river = []
#         self.visited = [[False] * len(self.matrix[0]) for _ in range(len(self.matrix))]
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[0])):
#                 if self.visited[i][j]:
#                     continue
#                 self.visited[i][j] == True
                
#                 if self.matrix[i][j] == 0:
#                     continue
#                 self.traverseThroughRiver(i,j)
#         print( self.river)
    
#     def traverseThroughRiver(self,i,j):
#         currentRiverSize = 0
#         self.stack.append((i,j))
#         while self.stack:
#             current = self.stack.pop()
#             i = current[0]
#             j = current[1]
            
#             if self.visited[i][j]:
#                 continue
#             self.visited[i][j] = True
#             if self.matrix[i][j] == 0:
#                 continue
            
#             currentRiverSize += 1
#             self.findNeighbours(i,j)
#         self.river.append(currentRiverSize)
    
#     def findNeighbours(self,i,j):
#         if i > 0 and self.visited[i-1][j] != True:
#             self.stack.append((i-1,j))
#         if i < len(self.matrix)-1 and self.visited[i+1][j] != True:
#             self.stack.append((i+1,j))
#         if j > 0 and self.visited[i][j-1] != True:
#             self.stack.append((i,j-1))
#         if j < len(self.matrix[0])-1 and self.visited[i][j+1] != True:
#             self.stack.append((i,j+1))
        
# if __name__ == '__main__':
#     matrix = [  [1, 0, 0, 1, 1],
#                 [0, 1, 1, 1, 0],
#                 [0, 0, 0, 0, 1],
#                 [1, 0, 0, 0, 1] ]
#     river = RiverSize(matrix)

# from collections import defaultdict,deque
# class Graph:
#     def __init__(self,routes):
#         self.graph_dict = defaultdict(list)
#         for vertex,edge in routes:
#             self.graph_dict[vertex].append(edge)
            
#     def get_path(self,start,end,path=[]):
#         path = path + [start]
#         if start == end:
#             return [path]
#         if start not in self.graph_dict:
#             return []
#         paths = []
#         for neighbour in self.graph_dict[start]:
#             if neighbour in self.graph_dict:
#                 p = self.get_path(neighbour,end,path)
#                 for i in p:
#                     paths.append(i)
#         return paths 
    
#     def get_shortest(self,start,end):
#         q = deque([(start,[start])])
#         while q:
#             current, path = q.popleft()
            
#             if current == end:
#                 return path
#             for neighbour in self.graph_dict[current]:
#                 if neighbour not in path:
#                     q.append((neighbour,path+[neighbour]))
#         return False
    
#     def dfs(self,start):
#         stack = deque()
#         stack.append(start)
#         path = []
#         visited = set()
#         while stack:
#             current = stack.pop()
#             if current not in visited:
#                 visited.add(current)
#                 path.append(current)
                
#                 for neighbour in self.graph_dict[current]:
#                     stack.append(neighbour)
#         return path
        
#     def display(self):
#         print(dict(self.graph_dict))
        
        
# if __name__ == '__main__':
#     routes = [
#         ('Mumbai','Paris'),
#         ('Mumbai','Dubai'),
#         ('Paris','Dubai'),
#         ('Paris','New york'),
#         ('Dubai','New york'),
#         ('New york','Torrento'),
#     ]
#     graph = Graph(routes)
#     graph.display()
#     # print(graph.get_path('Mumbai','New york'))
#     # print(graph.get_shortest('Mumbai','New york'))
#     print(graph.dfs('Mumbai'))

# import networkx as nx
# import matplotlib.pyplot as plt

# # Create a directed graph
# graph = nx.DiGraph()

# # Add edges with weights
# edges = [
#     ("A", "B", 1),
#     ("A", "C", 4),
#     ("B", "C", 2),
#     ("B", "D", 6),
#     ("C", "D", 3),
# ]
# graph.add_weighted_edges_from(edges)

# # Run Dijkstra's algorithm to get shortest paths
# source = "A"
# distances = nx.single_source_dijkstra_path_length(graph, source)
# shortest_paths = nx.single_source_dijkstra_path(graph, source)

# # Visualize the graph
# pos = nx.spring_layout(graph)  # Layout for better visualization
# plt.figure(figsize=(8, 6))

# # Draw the graph
# nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
# labels = nx.get_edge_attributes(graph, "weight")
# nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color="red", font_size=12)

# # Highlight shortest paths
# for target, path in shortest_paths.items():
#     edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
#     nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color="green", width=2)

# plt.title(f"Shortest Paths from Node '{source}'", fontsize=16)
# plt.show()

from collections import deque
class River :
    def __init__(self,matrix):
        self.matrix = matrix
        self.visited = [[False]*len(self.matrix[0]) for _ in range(len(self.matrix))]
        self.riverSize = []
        self.riv()
    def riv(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 0:
                    self.visited[i][j] = True
                    continue
                if self.visited[i][j]:
                    continue
                self.calculateSize(i,j)
        return self.riverSize
    def calculateSize(self,i,j):
        current_size = 0
        self.s = deque()
        self.s.append((i,j))
        while self.s:
            i,j = self.s.pop()
            if self.matrix[i][j] == 0:
                continue
            if self.visited[i][j] :
                continue
            self.visited[i][j] = True
            current_size += 1
            self.findNeighbours(i,j)
        self.riverSize.append(current_size)
            
    def findNeighbours(self,i,j):
        if i > 0 and not self.visited[i-1][j]:
            self.s.append((i-1,j))
        if i < len(self.matrix)-1 and not self.visited[i+1][j]:
            self.s.append((i+1,j))
        if j > 0 and not self.visited[i][j-1]:
            self.s.append((i,j-1))
        if j < len(self.matrix[0])-1 and not self.visited[i][j+1]:
            self.s.append((i,j+1))
            
            
if __name__ == '__main__':
    matrix = [  [1, 0, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 0, 1] ]
    river = River(matrix)
    print(river.riv())