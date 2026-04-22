from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        ans = []

        for r in range(0, len(nums)):

            # if r = 4 and k = 2. window is [3,4]. Hence 2 should be popped. so <=
            if q and q[0] <= r-k:
                q.popleft()
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            if r-k+1 >= 0:
                ans.append(nums[q[0]])
        
        return ans
