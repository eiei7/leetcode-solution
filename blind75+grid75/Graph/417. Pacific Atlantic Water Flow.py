"""
Method: dfs
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(r, c, visited, height): #O(m * n)
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or heights[r][c] < height:
                return 
            
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            
        for i in range(m): # O(m)
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n - 1, atl, heights[i][n - 1])
        for i in range(n): # O(n)
            dfs(0, i, pac, heights[0][i])
            dfs(m - 1, i, atl, heights[m - 1][i])
        
        res = []
        for (r, c) in pac:
            if (r, c) in atl:
                res.append([r, c]) 
        
        return res

#Time Complexity: O(n * m) #rows * cols
#Space Complexity: O(n * m)