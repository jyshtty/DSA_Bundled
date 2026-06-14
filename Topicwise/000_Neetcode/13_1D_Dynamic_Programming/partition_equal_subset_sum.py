"""
Problem: Partition Equal Subset Sum
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Description:
    Given a non-empty integer array nums, return true if the array can be
    partitioned into two subsets with equal sum.

Examples:
    Input:  nums = [1,5,11,5]    Output: True  ([1,5,5] and [11])
    Input:  nums = [1,2,3,5]     Output: False

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}  # set of achievable sums using numbers seen so far

        for num in nums:
            # iterate in a new set to avoid using num twice in the same pass
            dp = dp | {s + num for s in dp if s + num <= target}
            if target in dp:
                return True

        return False
