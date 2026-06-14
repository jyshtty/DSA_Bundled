"""
Problem: Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Description:
    Given a 1-indexed sorted array of integers numbers, find two numbers
    that add up to target. Return their indices (1-indexed). Each input
    has exactly one solution and you may not use the same element twice.
    Must use only O(1) extra space.

Examples:
    Input:  numbers = [2, 7, 11, 15], target = 9    Output: [1, 2]
    Input:  numbers = [2, 3, 4],      target = 6    Output: [1, 3]
    Input:  numbers = [-1, 0],        target = -1   Output: [1, 2]

Constraints:
    2 <= numbers.length <= 3 * 10^4
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    Exactly one valid answer exists.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # convert to 1-indexed
            elif total < target:
                left += 1   # sum too small, move left pointer right to increase it
            else:
                right -= 1  # sum too large, move right pointer left to decrease it

        return []
