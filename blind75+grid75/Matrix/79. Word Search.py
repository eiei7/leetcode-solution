"""
Method: hashset + dfs
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        
        def dfs(i, j, pos):
            if pos == len(word):
                return True
            #i, j -> board
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[pos] or (i, j) in visited:
                return False
            
            visited.add((i, j))
            res = dfs(i - 1, j, pos + 1) or dfs(i + 1, j, pos + 1) or dfs(i, j + 1, pos + 1) or dfs(i, j - 1, pos + 1)
            visited.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

#TC: O(m * n * 4^len(word))
#SC: O(len(word))
