"""
Method: using an extra space
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rowzero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowzero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        if rowzero:
            for j in range(n):
                matrix[0][j] = 0

#TC: O(m * n)
#SC: O(1)

"""
Method: hashset
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rowzero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowzero = True
        #先处理非第一行和第一列的元素，因为第一行和第一列元素需要作为判断依据（不能全置0先）
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:#在便利所有元素时，通过判断该行/列的第一个元素是不是0来决定要不要对其进行置零
                    matrix[i][j] = 0
        #处理第一列
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        #处理第一行
        if rowzero:
            for j in range(n):
                matrix[0][j] = 0

#TC: O(m * n)
#SC: O(1)
