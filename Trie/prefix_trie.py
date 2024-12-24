class TrieNode:
    def __init__(self):
        self.children = {}

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
        self.endSymbol = '*'
    
    def populatePrefixTree(self,words):
        for word in words:
            self.insertPrefixEndingAt(word)
    
    def insertPrefixEndingAt(self,word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.children[self.endSymbol] = word
    
    def contains(self,prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
    
    def autoComplete(self,prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return []
            node = node.children[letter]
        return self.collectAllWords(node)
        
    def collectAllWords(self,node):
        words = []
        for letter,child in node.children.items():
            if letter == self.endSymbol:
                words.append(child)
            else:
                words.extend(self.collectAllWords(child))
        return words
    
if __name__ == '__main__':
    trie = PrefixTrie()
    words = ['mango', 'mangi', 'manual', 'mantle', 'manna']
    trie.populatePrefixTree(words)
    print(trie.contains('man'))
    print(trie.autoComplete('mang'))

    # Test if prefixes exist
    # print(trie.contains("ma"))    # True
    # print(trie.contains("man"))   # True
    # print(trie.contains("manna")) # True
    # print(trie.contains("anna")) # False