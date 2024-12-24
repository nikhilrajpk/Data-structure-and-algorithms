# class TrieNode:
#     def __init__(self):
#         self.children = {}
        
# class PrefixTrie:
#     def __init__(self):
#         self.root = TrieNode()
#         self.endSymbol = '*'
#     def populateTrie(self,words):
#         for word in words:
#             self.prefixEndsBy(word)
            
#     def prefixEndsBy(self,word):
#         node = self.root
#         for letter in word:
#             if letter not in node.children:
#                 node.children[letter] = TrieNode()
#             node = node.children[letter]
#         node.children[self.endSymbol] = word
    
#     def autoComplete(self,word):
#         node = self.root
#         for letter in word:
#             if letter not in node.children:
#                 return False
#             node = node.children[letter]
#         return self.collectAllWords(node)
        
#     def collectAllWords(self,node):
#         words = []
#         for letter, child in node.children.items():
#             if letter == self.endSymbol:
#                 words.append(child)
#             else:
#                 words.extend(self.collectAllWords(child))
#         return words
    
# if __name__=='__main__':
#     words = ['man','mango','mangl','manna']
#     prefix = PrefixTrie()
#     prefix.populateTrie(words)
#     print(prefix.autoComplete('man'))

from collections import defaultdict,deque
class Graph:
    def __init__(self,elements):
        self.graph_dict = defaultdict(list)
        
        for vertex, edge in elements:
            self.graph_dict[vertex].append(edge)
        
    def bfs(self,start):
        que = deque([start])
        path = []
        visited = set()
        while que:
            current = que.popleft()
            if current not in visited:
                visited.add(current)
                path.append(current)
                
                for neighbour in self.graph_dict[current]:
                    que.append(neighbour)
        return path
    
    def display(self):
        print(dict(self.graph_dict))

if __name__ == '__main__':
    routes = [
        ('mumbai','paris'),
        ('mumbai','dubai'),
        ('paris','dubai'),
        ('paris','new york'),
        ('dubai','new york'),
        ('new york','torrento'),
    ]
    r = Graph(routes)
    r.display()
    print(r.bfs('mumbai'))