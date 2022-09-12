"""
Method: dfs(recursion)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        self.visited = set()
        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in self.visited or grid[i][j] == '0':
                return
            
            self.visited.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in self.visited and grid[i][j] == '1':#O(m * n)
                    dfs(i, j)
                    res += 1
        return res

#Time Complexity: O(m * n) # under the worst situation
#Space Complexity: O(m * n)

"""
Method: dfs(interation)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()#全局
        
        def dfs(i, j):
            q = deque()#对应每一个grid[][]来说，q需要重新更新
            q.append((i, j))
            visited.add((i, j))
            
            while q:
                d_i, d_j = q.pop() # bfs using popleft
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for cre_i, cre_j in directions:
                    cur_i = d_i + cre_i
                    cur_j = d_j + cre_j
                    if cur_i in range(m) and cur_j in range(n) and (cur_i, cur_j) not in visited and grid[cur_i][cur_j] == '1':
                        q.append((cur_i, cur_j))
                        visited.add((cur_i, cur_j))
                 
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res

