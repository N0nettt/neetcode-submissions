class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest = 0
        dp = {}

        def rec(i,j):
            if (i, j) in dp:
                return dp[(i, j)]

            val = matrix[i][j]
            res = 1
            
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < len(matrix) and nj >= 0 and nj < len(matrix[0]) and matrix[ni][nj] > val:
                    res = max(res, 1 + rec(ni, nj))
            
            dp[i, j] = res
            return dp[i, j]

            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, rec(i, j))
        return longest

        
            
