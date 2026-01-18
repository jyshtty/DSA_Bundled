# leetcode 34
# Problem: Find the first and last occurrence of a target value in a sorted array
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the first (leftmost) occurrence of target
        def first():
            high = len(nums) - 1
            low = 0
            res = -1
            
            # Binary search to find leftmost occurrence
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    res = mid     # Save position instead of returning immediately
                    high = mid - 1  # Continue searching in left half to find first occurrence

                elif target < nums[mid]:
                    high = mid - 1

                elif target > nums[mid]:
                    low = mid + 1

            return res

        # Helper function to find the last (rightmost) occurrence of target
        def second():
            high = len(nums) - 1
            low = 0
            res = -1
            
            # Binary search to find rightmost occurrence
            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    res = mid  # Save position instead of returning immediately
                    low = mid + 1  # Continue searching in right half to find last occurrence

                elif target < nums[mid]:
                    high = mid - 1

                elif target > nums[mid]:
                    low = mid + 1

            return res

        # Find the leftmost occurrence of target
        l = first()
        # Find the rightmost occurrence of target
        r = second()

        # Return array with [first occurrence, last occurrence]
        return [l, r]