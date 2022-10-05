from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        q = collections.deque()
        visit = set()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i, j])
                    visit.add((i, j))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = distance
                for d_r, d_c in directions:
                    new_r, new_c = r + d_r, c + d_c
                    if (new_r) in range(m) and (new_c) in range(n) and (new_r, new_c) not in visit and rooms[new_r][new_c] != -1:
                        q.append([new_r, new_c])
                        visit.add((new_r, new_c))
            distance += 1
        return rooms

#TC:O(mn)
#SP:O(mn)