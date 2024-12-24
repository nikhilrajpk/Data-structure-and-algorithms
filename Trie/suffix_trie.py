class TrieNode:
    def __init__(self):
        self.children = {}

class SuffixTrie:
    def __init__(self):
        self.root = TrieNode()
        self.endsymbol = '*'
    
    def populateSuffixTrie(self,string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i,string)
    
    def insertSubstringStartingAt(self,idx,string):
        node = self.root
        for i in range(idx,len(string)):
            letter = string[i]
            if letter not in node.children:
                newNode = TrieNode()
                node.children[letter] = newNode
            node = node.children[letter]
            
            # print(self.root.children)
        node.children[self.endsymbol] = None
    
    def contains(self,string):
        node = self.root
        for i in range(len(string)):
            letter = string[i]
            if letter not in node.children:
                return False
            node = node.children.get(letter)
        
        return self.endsymbol in node.children

if __name__ == '__main__':
    trie = SuffixTrie()
    trie.populateSuffixTrie('manna')
    trie.populateSuffixTrie('mina')
    print(trie.contains('mana'))