
class Solution:
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        visited = set()

        def bracktrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                    r > row - 1 or c > col - 1 or
                    board[r][c] != word[i] or
                    (r, c) in visited): # to avoid circle. To avoid same position twice
                return False

            visited.add((r, c))
            res = (bracktrack(r + 1, c, i + 1) or
                   bracktrack(r - 1, c, i + 1) or
                   bracktrack(r, c + 1, i + 1) or
                   bracktrack(r, c - 1, i + 1))
            visited.remove((r, c))
            return res

        for r in range(row):
            for c in range(col):
                if bracktrack(r, c, 0):
                    return True
        return False

