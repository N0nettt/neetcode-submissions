class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        i, mid = 0, len(matrix) // 2
    
        while i < mid:
            temp = matrix[i]
            matrix[i] = matrix[len(matrix)-1-i] 
            matrix[len(matrix)-1-i] = temp
            i+=1

        i = 0
        for i in range(r):
            for j in range(c):
                if i == j or j < i:
                    continue
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        



        
