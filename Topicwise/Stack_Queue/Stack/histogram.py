class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        # This step is very important. n because if there is no smaller element to the right of current element then we can consider the right boundary of rectangle as n. 
        # Similarly, if there is no smaller element to the left of current element then we can consider the left boundary of rectangle as -1. This way we can avoid extra checks in our code.
        smallest_from_right = [n] * n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                largest_from_right[i] = stack[-1] 
            stack.append(i)
        
        smallest_from_left = [-1] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                largest_from_left[i] = stack[-1] 
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, (largest_from_right[i] - largest_from_left[i] - 1) * heights[i])
        
        return ans


