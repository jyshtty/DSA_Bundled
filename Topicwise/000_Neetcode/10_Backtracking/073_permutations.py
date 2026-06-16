"""
Problem: Permutations
Link: https://leetcode.com/problems/permutations/

Description:
    Given an array nums of distinct integers, return all possible permutations.
    You can return the answer in any order.

Examples:
    Input:  nums = [1,2,3]    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Input:  nums = [0,1]      Output: [[0,1],[1,0]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All integers are unique.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, remaining):
            if not remaining:
                result.append(current[:])
                return
            for i in range(len(remaining)):
                current.append(remaining[i])
                # pass remaining without the chosen element to prevent reuse
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()

        backtrack([], nums)
        return result
