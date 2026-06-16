"""
Problem: Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/

Description:
    Given an array nums of n+1 integers where each value is in [1, n],
    there is exactly one repeated number. Find it without modifying the
    array and using only O(1) extra space.

Examples:
    Input:  nums = [1,3,4,2,2]    Output: 2
    Input:  nums = [3,1,3,4,2]    Output: 3

Constraints:
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    Only one value is repeated (may appear more than twice).
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat array values as "next" pointers — duplicate causes a cycle (Floyd's algorithm)
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # phase 2: find cycle entry point — reset one pointer to start
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
