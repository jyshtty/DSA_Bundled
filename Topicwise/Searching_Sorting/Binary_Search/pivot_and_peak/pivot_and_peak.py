from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # descending slope → peak is on left (including m)
            if nums[m] > nums[m + 1]:
                r = m
            else:
                # ascending slope → peak is on right
                l = m + 1

        return l


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # right half sorted → min is on left (including m)
            if nums[m] < nums[r]:
                r = m
            else:
                # min is strictly on right
                l = m + 1

        return nums[l]
