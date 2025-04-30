"""

Problem Description

Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom and columns are numbered from left to right.
Sum may be large so return the answer mod 109 + 7.


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M



Input Format
The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.



Output Format
Return an integer array containing the submatrix sum for each query.



Example Input
Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
Input 2:

 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]


Example Output
Output 1:

 [12, 28]
Output 2:

 [22, 19]


Example Explanation
Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.

 """
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers

    def prefix_sum(self,A):
        ls = []
        for i in range(len(A)):
            sum = 0
            temp = []
            for j in range(len(A[0])):
                sum = sum + A[i][j]
                if len(ls) > 0:
                    temp.append(sum + ls[i -1][j])
                else:
                    temp.append(sum)
            ls.append(temp)
        return ls

    def solve(self, A, B, C, D, E):
        ls = self.prefix_sum(A)
        result = []
        for k in range(len(B)):
            i,j,p,q =  B[k]-1, C[k]-1, D[k]-1, E[k]-1
            if i > 0 and j > 0:
                result.append(ls[p][q] - ls[p][j-1] - ls[i-1][q] + ls[i-1][j-1])
            elif i == 0 and j > 0:
                result.append(ls[p][q] - ls[p][j - 1])
            elif i > 0 and j == 0:
                result.append(ls[p][q] - ls[i-1][q])
            else:
                result.append(ls[p][q])
        return result

if __name__ == "__main__":
    A = [[5, 17, 100, 11],
         [0, 0, 2, 8]]
    B = [1, 1]
    C = [1, 4]
    D = [2, 2]
    E = [2, 4]
    obj = Solution()
    print(obj.solve(A,B,C,D,E))



