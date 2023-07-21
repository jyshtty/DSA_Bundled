# Problem Description
# There are N jobs to be done, but you can do only one job at a time.
#
# Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.
#
# Your aim is to select jobs in such a way so that you can finish the maximum number of jobs.
#
# Return the maximum number of jobs you can finish.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= A[i] < B[i] <= 109
#
#
#
# Input Format
# The first argument is an integer array A of size N, denoting the start time of the jobs.
# The second argument is an integer array B of size N, denoting the finish time of the jobs.
#
#
#
# Output Format
# Return an integer denoting the maximum number of jobs you can finish.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 5, 7, 1]
#  B = [7, 8, 8, 8]
# Input 2:
#
#  A = [3, 2, 6]
#  B = [9, 8, 9]

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, B, A):
        for i in range(len(A)):
            A[i] = (A[i], i)
        A.sort()


        new_B = [0] * len(B)
        for i in range(len(B)):
            new_B[i] = B[A[i][1]]

        new_A = [i[0] for i in A]
        ans = 1

        i = 0
        j = 1
        while i < len(new_A) - 1 and j < len(new_B):
            if new_A[i] <= new_B[j]:
                ans += 1
                i = j
            j += 1
        return ans

A = [1, 5, 7, 1]
B = [7, 8, 8, 8]
obj = Solution()
print(obj.solve(A, B))