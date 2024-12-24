class TrieNode:
    def __init__(self):
        self.children = {}

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
        self.endSymbol = '*'
        
    def populatePrefixTrie(self,words):
        for word in words:
            self.prefixEndsAt(word)
    
    def prefixEndsAt(self,word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.children[self.endSymbol] = word
    
    def contains(self,word):
        node = self.root
        for letter in word :
            if letter not in node.children:
                return False
            node = node.children[letter]
        return self.endSymbol in node.children
    
    def autoComplete(self,prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return self.collectAllWords(node)
    def collectAllWords(self,node):
        words = []
        for letter, child in node.children.items():
            if letter == self.endSymbol:
                words.append(child)
            else:
                words.extend(self.collectAllWords(child))
        return words
    def remove(self,word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        if self.endSymbol not in node.children:
            return 'cannot delete this prefix.'
        else:
            del node.children[self.endSymbol]
    
if __name__ == '__main__':
    prefix = PrefixTrie()
    prefix.populatePrefixTrie(['mango', 'man', 'manual', 'mantle', 'manna'])
    print(prefix.contains('man'))
    print(prefix.autoComplete('man'))
    print(prefix.remove('mango'))
    print(prefix.contains('man'))
    print(prefix.autoComplete('man'))