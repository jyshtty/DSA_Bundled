"""
Pairs With Given Xor
Problem Description

Given an 1D integer array A containing N distinct integers.

Find the number of unique pairs of integers in the array whose XOR is equal to B.

NOTE:

Pair (a, b) and (b, a) is considered to be same and should be counted once.


Problem Constraints
1 <= N <= 105

1 <= A[i], B <= 107



Input Format
First argument is an 1D integer array A.

Second argument is an integer B.



Output Format
Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.



Example Input
Input 1:

 A = [5, 4, 10, 15, 7, 6]
 B = 5
Input 2:

 A = [3, 6, 8, 10, 15, 50]
 B = 5


Example Output
Output 1:

 1
Output 2:

 2


Example Explanation
Explanation 1:

 (10 ^ 15) = 5
Explanation 2:

 (3 ^ 6) = 5 and (10 ^ 15) = 5
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dict01 = {}
        count = 0
        for i in range(len(A)):
            if A[i] in dict01:
                continue
            elif B ^ A[i] not in dict01:
                dict01[A[i]] = 1
            elif dict01[B ^ A[i]] == 'already counted':
                continue
            else:
                count = count + 1
                dict01[B ^ A[i]] = 'already counted'
        return count, dict01
# (2, {8: 1, 10: 'already counted', 3: 'already counted', 50: 1})
#
if __name__ == "__main__":
    A = [3, 6, 8, 10, 15, 50,6,6,3,6]
    B = 5
    obj = Solution()
    print(obj.solve(A,B))

