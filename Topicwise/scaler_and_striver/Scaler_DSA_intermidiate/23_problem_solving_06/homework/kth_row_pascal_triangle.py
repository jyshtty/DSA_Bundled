"""
Problem Description

Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
Note: k is 0 based. k = 0, corresponds to the row [1].

Note: Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        prev = 1
        ls = [1]

        for i in range(1, N + 1):
            curr = (prev * (N - i + 1)) // i
            ls.append(curr)
            prev = curr
        return ls

if __name__ == "__main__":
    N = 0
    obj = Solution()
    print(obj.getRow(N))



