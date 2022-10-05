class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(i, j, visit, preheight):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in visit or heights[i][j] < preheight:
                return
            
            visit.add((i, j))
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])
            
        for i in range(m):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, n - 1, atl, heights[i][n - 1])
        for i in range(n):
            dfs(0, i, pac, heights[0][i])
            dfs(m - 1, i, atl, heights[m - 1][i])
            
        res = []
        for i, j in pac:
            if (i, j) in atl:
                res.append([i, j])
        return res