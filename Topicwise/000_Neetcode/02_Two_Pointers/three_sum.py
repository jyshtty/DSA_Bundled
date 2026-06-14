"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/

Description:
    Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
    such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
    The solution set must not contain duplicate triplets.

Examples:
    Input:  nums = [-1, 0, 1, 2, -1, -4]    Output: [[-1, -1, 2], [-1, 0, 1]]
    Input:  nums = [0, 1, 1]                 Output: []
    Input:  nums = [0, 0, 0]                 Output: [[0, 0, 0]]

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # if smallest possible triplet is positive, no solution exists beyond this point
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # skip duplicates for second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
