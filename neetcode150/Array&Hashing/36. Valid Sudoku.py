"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        row = collections.defaultdict(set)#hashset
        col = collections.defaultdict(set)
        cube = collections.defaultdict(set)# (i//3,j//3) as key
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in cube[(i // 3, j // 3)]:
                        return False
                    row[i].add(board[i][j])#名为row的hashet以当前行i为key,存储元素值
                    col[j].add(board[i][j])
                    cube[(i // 3, j // 3)].add(board[i][j])
        return True

#TC:O(m * n) = O(9^2)
#SP:O(m * n + (m//3)*(n//3))
"""