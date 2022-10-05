class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        visit = set()
        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in visit or grid[i][j] == 0:
                return
            self.count += 1
            visit.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        self.res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visit:
                    self.count = 0
                    dfs(i, j)
                    self.res = max(self.res, self.count)
        return self.res

#TC:O(n*m*max(self.res))
#SP:O(n*m)