# leetcode 18: 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# https://leetcode.com/problems/4sum/
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Approach: Two pointers
# Time Complexity: O(n^3)
# Space Complexity: O(1)
# Implementation:


# Approach 1

# 3 pointer and binary search
#
# 1. First sort the array
# 2. fix i at 0
# 3. j at i+1
# 4. k at j+1
#
# 5. iff = target - nums[i] - nums[j] - nums[k]
#
# 6. use binary search to find diff in elements after k

# 7. when you get put the puad i.e [nums[i], nums[j], nums[k], another elem] in set

# 8. return set

# TC - N3 * logN + NlogN(for sorting)


# Approach 2

# 1. First sort the array
# 2. fix i at 0
# 3. j at i+1
# 4. set 2 more pointers. Left and Right. Left = j+1 and right = len(array) - 1
# 5.
# TC - N3

class Solution:
    def fourSum(self, nums, target):
        l = len(nums)
        ans = set()
        nums.sort()
        for i in range(l - 1 - 1 - 1):
            for j in range(i + 1, l - 1 - 1):
                left = j + 1
                right = l - 1
                diff = target - nums[i] - nums[j]

                while left < right:
                    if nums[left] + nums[right] == diff:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        right -= 1
                        left += 1
                    elif nums[left] + nums[right] > diff:
                        right -= 1
                    else:
                        left += 1
        return [list(i) for i in ans]

obj = Solution()
print(obj.fourSum([1,0,-1,0,-2,2], 0))