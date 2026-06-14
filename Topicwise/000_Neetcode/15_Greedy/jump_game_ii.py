"""
Problem: Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/

Description:
    Return the minimum number of jumps to reach the last index.
    You can always reach the last index.

Examples:
    Input:  nums = [2,3,1,1,4]    Output: 2  (jump to index 1, then to last)
    Input:  nums = [2,3,0,1,4]    Output: 2

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0   # end of the range covered by the current number of jumps
        farthest = 0      # farthest index reachable within the current range

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1        # must take a jump to progress beyond current_end
                current_end = farthest

        return jumps
