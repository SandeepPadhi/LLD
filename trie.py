
class TrieNode:
    def __init__(self):
        self.is_end=False 
        self.children={}
    
class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        node=self.root 
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True 
    
    def search(self,word):
        node=self.root 
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return node.is_end
    
    def prefix(self,word):
        node=self.root 
        for ch in word:
            if ch not in node.children:
                return False 
            node=node.children[ch] 
        return True
    
# Example Usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("appl"))   # Output: False
print(trie.search("banana")) # Output: True
print(trie.prefix("app")) # Output: True
print(trie.prefix("ban")) # output: True
print(trie.prefix("bap")) #output: False