# Approach
# 1. Sort the  array
# 2. Do a func call for # All subsets that include nums[i]
# 3. Check if nums[i] == nums[i+1], then i += 1
# 4.  Do a func call for # All subsets that do not include nums[i]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []
        nums.sort()

        def backtrack(index, temp):
            if index == len(nums):
                ans.append(temp.copy())
                return

            # All subsets that include nums[i]
            temp.append(nums[index])
            backtrack(index + 1, temp)
            temp.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            # All subsets that do not include nums[i]
            backtrack(index + 1, temp)

        backtrack(0, temp)
        return ans