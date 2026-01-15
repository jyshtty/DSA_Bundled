# leetcode 75: Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# https://leetcode.com/problems/sort-colors/
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Approach: Dutch National Flag algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


arr = [0,1,1,0,1,2,1,2,0,0,1]
def sort_all(arr):
  low = 0
  mid = 0
  high = len(arr) - 1
  while (high>=mid):
    if arr[low] == 0 and arr[mid] == 0:
      low += 1
      mid += 1
    elif arr[mid] == 0:
      arr[low], arr[mid] = arr[mid], arr[low]
      mid += 1
      low += 1
    elif arr[mid] == 2:
      arr[high], arr[mid] = arr[mid], arr[high]
      high -= 1
    else:
      mid += 1
  return arr

print(sort_all(arr))
