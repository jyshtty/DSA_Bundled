"""
Problem Description

You are given an array A having N integers.

You have to divide / split the array into 2 subsequence partitions such that:

Both the partitions are non-empty.
Each integer A[i] in the array belongs to exactly one of the two partitions.
Absolute difference between the maximum of first partition and the minimum of second partition is minimum possible.
If B and C represent the two partitions, then size(B) >= 1, size(C) >= 1 and |max(B) - min(C)| is minimum possible. You have to find such a spliting and tell the minimum value of |max(B) - max(C)|.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        min_diff = float('inf')
        for i in range(len(A)-1):
            diff = abs(A[i+1] - A[i])
            min_diff = min(diff, min_diff)
        return min_diff

if __name__ == "__main__":
    A = [2, 1, 3, 2, 4, 3]
    obj = Solution()
    print(obj.solve(A))



