"""
Given a binary matrix A of integers 0 and 1, of size N x M.

Find and return the indices of the rows which are duplicate of rows which are already present in the matrix.

If row[i] and row[j] are same and i < j then answer will contain only index j.

Note: Rows are numbered from top to bottom and columns are numbered from left to right. There will be at least one duplicate row in the matrix.


Input Format

The first argument given is the integer matrix A.
Output Format

Return the indices of the rows in the form of an integer array.
Constraints

2 <= N, M <= 1000
0 <= A[i] <= 1
For Example

Input 1:
    A = [   [1, 0, 0]
            [0, 1, 0]
            [0, 1, 0]   ]
Output 1:
    [3]

Input 2:
    A = [   [1, 1, 1, 0]
            [0, 0, 0, 1]
            [1, 1, 1, 0]
            [0, 0, 0, 1]    ]
Output 2:
    [3, 4]
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        s = set()
        ls = []
        for i in range(len(A)):
            decimal = 0
            for j in range(len(A[i])):
                decimal += A[i][j] * pow(2, j)
            if decimal not in s:
                s.add(decimal)
            else:
                ls.append(i + 1)
        return ls


if __name__ == "__main__":
    A = [[1, 1, 1, 0],
         [0, 0, 0, 1],
         [1, 1, 1, 0],
         [0, 0, 0, 1]]
    obj = Solution()
    print(obj.solve(A))
