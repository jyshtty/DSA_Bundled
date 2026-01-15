# leetcode 34: Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Approach: Binary Search
# Perform two binary searches: one to find the first occurrence and one to find the last occurrence of the target.
# For the first occurrence, when target is found, move the high pointer to mid-1 to search in the left half.
# For the last occurrence, when target is found, move the low pointer to mid+1 to search in the right half.
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Implementation:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first():
            high = len(nums) - 1
            low = 0
            res = -1
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    res = mid     # only change - instead of returning mid save it in res
                    high = mid - 1  # and make high to mid -1

                elif target < nums[mid]:
                    high = mid - 1

                elif target > nums[mid]:
                    low = mid + 1

            return res

        def second():
            high = len(nums) - 1
            low = 0
            res = -1
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    res = mid  # only change - instead of returning mid save it in res
                    low = mid + 1  # and make high to mid -1

                elif target < nums[mid]:
                    high = mid - 1

                elif target > nums[mid]:
                    low = mid + 1

            return res

        l = first() # to find left first occurance.
        r = second() # to find right first occurance.

        return [l, r]