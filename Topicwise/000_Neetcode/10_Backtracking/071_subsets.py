"""
Problem: Subsets
Link: https://leetcode.com/problems/subsets/

Description:
    Given an integer array nums of unique elements, return all possible subsets.
    The solution set must not contain duplicate subsets. Return in any order.

Examples:
    Input:  nums = [1,2,3]    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    Input:  nums = [0]        Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All nums are unique.
"""

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
