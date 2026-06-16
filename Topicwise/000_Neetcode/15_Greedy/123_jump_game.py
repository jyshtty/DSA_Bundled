"""
Problem: Jump Game
Link: https://leetcode.com/problems/jump-game/

Description:
    Given an array where nums[i] is the max jump length from index i,
    return true if you can reach the last index.

Examples:
    Input:  nums = [2,3,1,1,4]    Output: True
    Input:  nums = [3,2,1,0,4]    Output: False

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # the farthest index reachable so far

        for i, jump in enumerate(nums):
            if i > farthest:
                return False  # current index is unreachable
            farthest = max(farthest, i + jump)

        return True
