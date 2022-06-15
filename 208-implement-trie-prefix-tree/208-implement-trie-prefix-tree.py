class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: # if char does not exist in tree
                cur.children[c] = TrieNode() #Create new node for char
            cur = cur.children[c]
        cur.endOfWord = True # mark the end of word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children: # if char does not exist in tree
                return False
            cur = cur.children[c]
        return cur.endOfWord # Return true is there is a endofWord, otherwise false

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

