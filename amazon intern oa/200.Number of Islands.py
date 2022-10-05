class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or (i,j) in self.visited or grid[i][j] != '1':
                return
            self.visited.add((i,j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        res = 0
        self.visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in self.visited and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res