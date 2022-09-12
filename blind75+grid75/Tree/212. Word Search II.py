"""
Method1: dictionary trie
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.insert(w)
        
        m, n = len(board), len(board[0])
        res = set()
        visited = set()
        def dfs(i, j, node, word):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in visited or board[i][j] not in node.children:
                return
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.end:
                res.add(word)
            visited.add((i, j))
            dfs(i, j - 1, node, word)
            dfs(i, j + 1, node, word)
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            visited.remove((i, j))
            
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        return list(res)

