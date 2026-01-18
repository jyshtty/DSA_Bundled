# leetcode 53: Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# https://leetcode.com/problems/maximum-subarray/
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Approach: Kadane's algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


"""
Find maximum sum of a subarray in O(N)
"""

A = [-2,-3,4,-1,-2,1,5,-3]
def foo(A):
    sum_ = 0
    maxi = -float('inf')
    for x in A:
        sum_ = max(x, sum_ + x)   # Either start new subarray at x or extend
        maxi = max(maxi, sum_)
    return maxi

print(foo(A))


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = float('-inf')
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            sum = sum + nums[i]

            if sum > maxi:
                maxi = max(sum, maxi)

            if sum < 0:
                sum = 0
        return maxi



# import  protgres
#
# connection = protgres.connect('connection'string)
#
# mbr = conection.excute('select * from mbr')
