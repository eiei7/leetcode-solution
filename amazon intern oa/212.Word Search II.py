class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.insert(w)
        
        res = set()
        visit = set()
        def dfs(i, j, node, word):
            if i < 0 or i == m or j < 0 or j == n or (i,j) in visit or board[i][j] not in node.children:
                return
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.end:
                res.add(word)
            
            visit.add((i,j))
            dfs(i - 1, j, node, word)
            dfs(i + 1, j, node, word)
            dfs(i, j - 1, node, word)
            dfs(i, j + 1, node, word)
            visit.remove((i,j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i, j, root, "")
        return list(res)