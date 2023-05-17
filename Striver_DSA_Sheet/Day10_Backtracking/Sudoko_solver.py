# https://leetcode.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board):
        board = []

        def check(board, row, col, k):
            k = str(k)
            for i in range(9):
                if board[i][col] == k or board[row][i] == k:
                    return False
            new_r = row - row % 3
            new_c = col - col % 3

            for i in range(new_r, new_r + 3):
                for j in range(new_c, new_c + 3):
                    if board[i][j] == k:
                        return False
            return True

        def bracktrack(i):
            if i == 81:
                return True

            row = i // 9
            col = i % 9

            if board[row][col] != ".":
                return bracktrack(i + 1)

            for k in range(1, 10):
                if check(board, row, col, k):
                    board[row][col] = str(k)
                    if bracktrack(i + 1):
                        return True
                    board[row][col] = "."
            return False

        bracktrack(0)
        return board

if __name__ == "__main__":
    A =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    obj = Solution()
    print(obj.solveSudoku(A))