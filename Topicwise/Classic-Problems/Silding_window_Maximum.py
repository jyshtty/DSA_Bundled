# leetcode 239: Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# https://leetcode.com/problems/sliding-window-maximum/
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# Approach: Deque
# Use a deque to store indices of elements in decreasing order.
# For each element, remove from back if smaller, add current.
# Remove from front if out of window.
# The front is the max for the window.
# Time Complexity: O(n)
# Space Complexity: O(k)

# Implementation:

# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        from collections import deque 

        q = deque()
        ans = []

        l = len(nums)
        for i in range(l): # iterate through all elements

            if q and q[0] <= i - k: # step 1 - remove elements not within the window
                q.popleft()
            
            while q and nums[q[-1]] < nums[i]: # step 2 - maintain decreasing order in deque
                q.pop()
            
            q.append(i) # step 3 - add current element index to deque

            if i-k+1 >= 0: # step 4 - add maximum for current window to ans if window is valid.
                ans.append(nums[q[0]]) 

        return ans
        


from collections import deque
def sliding_window_maximum(arr, k):
    l = 0
    r = 0
    q = deque()
    output = []

    while r < len(arr):
        # 1. Maintain monotoneous decreasing array.
        while q and arr[q[-1]] < arr[r]:
            q.pop()
        q.append(r)

        # 2. Remove number from left of quque when it is not included in window.
        if l > q[0]:
            q.popleft()

        # 3. Add number to output only when r crosses window size. untill then only increment r.
        if r+1 >= k:
            output.append(arr[q[0]])
            l += 1
        r += 1

    return output

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
K = 3
# Output: 3 3 4 5 5 5 6

print(sliding_window_maximum(arr, K))



    