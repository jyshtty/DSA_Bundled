# leetcode 78: Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# https://leetcode.com/problems/subsets/
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Approach: Backtracking
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Implementation:


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []

        def generate(index, temp):
            if index == len(nums):
                ans.append(temp)
                return
            generate(index + 1, temp + [nums[index]])
            generate(index + 1, temp)
        generate(0, temp)
        return sorted(ans)


# By not passing temp as arguement
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []

        def generate(index):
            if index == len(nums):
                new = []
                for i in temp:
                    new.append(i)
                ans.append(new)
                return
            temp.append(nums[index])
            generate(index + 1)
            temp.pop()
            generate(index + 1)

        generate(0)

        return sorted(ans)

if __name__ == "__main__":
    nums = [1,2,3]
    obj = Solution()
    print(obj.subsets(nums))
