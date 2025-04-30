# leetcode 34
#

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