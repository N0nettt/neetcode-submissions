class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            val = matrix[i][j]
            res = 1

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > val:
                    res = max(res, 1 + dfs(ni, nj))
            
            dp[(i, j)] = res
            return res

        longest = 0
        for i in range(rows):
            for j in range(cols):
                longest = max(longest, dfs(i, j))

        return longest