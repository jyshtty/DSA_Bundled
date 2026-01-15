# leetcode 704: Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# https://leetcode.com/problems/binary-search/
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Approach: Binary search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Implementation:

class Solution:
    def search(self, nums, target):

        high = len(nums) - 1
        low = 0

        if high == low and target == nums[low]:
            return low

        while high >= low:
            mid = low + (high - low) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    obj = Solution()
    print(obj.search(nums, target))
