# leetcode 41: First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
# https://leetcode.com/problems/first-missing-positive/
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1

# Approach: Cycle Sort
# The idea is to place each number at its correct index if possible.
# For each number, if it's in range 1 to n, swap it to its correct position.
# Then, find the first index where nums[i] != i+1.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Implementation:

class Solution:
    def firstMissingPositive(self, nums):
        n=1
        nums=set(nums)
        while n in nums:
            n+=1
        return n
