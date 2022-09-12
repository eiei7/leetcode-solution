class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):#i = offset
                top, bottom = left, right #cuz square
                #save the topleft
                tmp = matrix[top][left + i]
                #topleft <- bottomleft
                matrix[top][left + i] = matrix[bottom - i][left]
                #bottomleft <- bottomright
                matrix[bottom - i][left] = matrix[bottom][right - i]
                #bottomright <- topright
                matrix[bottom][right - i] = matrix[top + i][right]
                #topright <- tmp
                matrix[top + i][right] = tmp
            left += 1
            right -= 1

#TC: O(n^2)
#SC: O(1)