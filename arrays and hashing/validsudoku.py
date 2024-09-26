from collections import defaultdict
class Solution:
    def isValidSudoku(self, board) -> bool:
        #using two hashsets is a good idea 
        # issue is the 3x3 situation
        # the idea is to make the 9 grids coordinates from 0 to  2 
        # and then get the actual row or column in the sudoku, and to integer dvision to deicede which square it should be in 
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key is a pair of value of rows and columns

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]: # if the current number is already inside the current row, its a dupe so  we return false and if we are already in a current column
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])