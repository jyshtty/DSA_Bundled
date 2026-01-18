# Question = Number of times it is right shifted.


# find index of minimum element ---------- find pivot - which is lowest number in list

# next = (mid+1) % N    to avoid index going byond length of array
# prev = (N + mid-1) % N       to avoid index going less than araay 0.

# if arr[mid] < arr[next]  and arr[mid] < arr[prev] return mid  ----- property of smallest number is both the number on it left and right side are larger than itself

# if arr[mid] > arr[0], low = mid + 1          coz always take the unsorted and discard the sorted part
# else: hogh = mid - 1

from typing import List

class Solution:
    def countRightShifts(self, arr: List[int]) -> int:
        n = len(arr)
        low, high = 0, n - 1

        while low <= high:
            # Case 1: array is already sorted
            if arr[low] <= arr[high]:
                return low  # smallest element index

            mid = low + (high - low) // 2
            next_idx = (mid + 1) % n # to avoid index going beyond length of array
            prev_idx = (mid - 1 + n) % n # to avoid index going less than 0

            # Case 2: mid is the minimum element
            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]: #  property of smallest number is both the number on it left and right side are larger than itself
                return mid

            # Case 3: left part is sorted → pivot is in right part
            if arr[mid] >= arr[low]: # always take the unsorted and discard the sorted part
                low = mid + 1 # move to right part, discard left part as it is sorted
            else:
                high = mid - 1

        return 0  # fallback (should never reach here)


# ------------------ DRIVER CODE ------------------
if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]

    solution = Solution()
    shifts = solution.countRightShifts(arr)

    print("Array:", arr)
    print("Number of right shifts:", shifts)
