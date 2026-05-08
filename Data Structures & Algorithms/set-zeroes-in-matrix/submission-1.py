class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeros = [[False] * len(matrix), [False] * cols]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros[0][i] = True
                    zeros[1][j] = True

        for i in range(rows):
            for j in range(cols):
                if zeros[0][i] == True or zeros[1][j] == True:
                    matrix[i][j] = 0

        