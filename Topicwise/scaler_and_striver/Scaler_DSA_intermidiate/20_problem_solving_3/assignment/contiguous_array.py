"""
Given an array of integers A consisting of only 0 and 1.

Find the maximum length of a contiguous subarray with equal number of 0 and 1.



Input Format

The only argument given is the integer array A.
Output Format

Return the maximum length of a contiguous subarray with equal number of 0 and 1.
Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 1
For Example

Input 1:
    A = [1, 0, 1, 0, 1]
Output 1:
    4
    Explanation 1:
        Subarray from index 0 to index 3 : [1, 0, 1, 0]
        Subarray from index 1 to index 4 : [0, 1, 0, 1]
        Both the subarrays have equal number of ones and equal number of zeroes.

Input 2:
    A = [1, 1, 1, 0]
Output 2:
    2
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        for i in range(len(A)):
            if A[i] == 0:
                A[i] = -1

        prefix_sum = [0] * len(A)
        for i in range(len(A)):
            prefix_sum[i] = A[i] + prefix_sum[i-1]

        dict01 = {0:[-1,-1]}
        maxi_diff = 0
        for i in range(len(A)):
            if prefix_sum[i] in dict01:
                dict01[prefix_sum[i]][1] = i
                maxi_diff = max((dict01[prefix_sum[i]][1] - dict01[prefix_sum[i]][0]),maxi_diff)
            else:
                dict01[prefix_sum[i]] = [i,i]
        return maxi_diff

if __name__ == '__main__':
    A = [ 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1 ]
    obj = Solution()
    print(obj.solve(A))
