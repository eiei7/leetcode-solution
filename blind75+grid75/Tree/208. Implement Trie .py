"""
Method1: dictionary trie
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.endofword = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return cur_node.endofword
        
    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#TC:O(n) # n = length of insert word or length of search word
#SC:O(1) #O(26) = O(1)

"""
Method2: Brute force
"""
class Trie:

    def __init__(self):
        self.res = []

    def insert(self, word: str) -> None:
        self.res.append(word)

    def search(self, word: str) -> bool:
        if word in self.res:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.res:
            i = 0
            flag = True
            while i < len(word) and i < len(prefix):
                if word[i] != prefix[i]:
                    flag = False
                    break
                i += 1
            if i == len(prefix) and flag:
                return True
        return False

#TC:O(m * n)
#SC:O(n)
