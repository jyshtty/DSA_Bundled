# Given a 2D matrix A of dimensions N x M consisting of 0s and 1s.
# A group of connected 1s forms an island. From a cell (i, j), we can visit any cell among the 4 cells surrounding it if that cell has value 1.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
            

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        
        return count

# (i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
# (i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
# (i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
# (i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
# (i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
# (i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
# (i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
# (i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
def isSafe(i, j):
    # row number is in range, column number
    # is in range and value is 1
    # and not yet visited
    return (i >= 0 and i < len(A) and
            j >= 0 and j < len(A[0]) and A[i][j])


def dfs(A, i, j):

    p = [-1, -1, 0, 1, 1, 1, 0, -1]
    q = [0, 1, 1, 1, 0, -1, -1, -1]

    for each in range(8):
        if isSafe(i + p[each], j + q[each]):
            A[i + p[each]][j + q[each]] = 0
            dfs(A, i + p[each], j + q[each])

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A[i][j] = 0
                    count += 1
                    dfs(A, i, j)
        return count, A

if __name__ == "__main__":
    A = [[0, 0, 1, 0, 1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1, 1, 1, 0, 1]]
    obj = Solution()
    print(obj.solve(A))
