class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                

                n = board[i][j]

                if n in row[i] or n in cols[j] or n in squares[(i//3, j//3)]:
                    return False
                
                row[i].append(n)
                cols[j].append(n)
                squares[(i//3, j//3)].append(n)
            
        return True