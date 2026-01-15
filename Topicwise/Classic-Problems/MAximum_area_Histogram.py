# leetcode 84: Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Example 2:
# Input: heights = [2,4]
# Output: 4

# Approach: Monotonic Stack
# For each bar, find the left and right smaller bars using stack.
# Area for each bar = height * (right_index - left_index - 1)
# Keep track of the maximum area.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Implementation:

class Solution:
    # @param A : list of integers
    # @return an integer
    def smallestToLeft(self, A):
        psedoindex = -1
        stack = []
        left = []
        for i in range(len(A)):
            while stack and stack[-1][0] >= A[i]:
                stack.pop()
            if not stack:
                left.append(psedoindex)
            else:
                left.append(stack[-1][1])
            stack.append([A[i], i])
        return left

    def smallestToRight(self, A):
        pseudo_index = len(A)
        stack = []
        right = []

        for i in range(len(A) - 1, -1, -1):
            while stack and stack[-1][0] >= A[i]:
                stack.pop()
            if not stack:
                right.append(pseudo_index)
            else:
                right.append(stack[-1][1])
            stack.append([A[i], i])
        return right[::-1]

    def largestRectangleArea(self, A):
        left = self.smallestToLeft(A)
        right = self.smallestToRight(A)

        width = []
        for i in range(len(left)):
            width.append(right[i] - left[i] - 1)
        area = []

        for i in range(len(width)):
            area.append(width[i] * A[i])
        print(A)
        print(left)
        print(right)
        print(width)
        print(area)
        return max(area)

obj = Solution()
print(obj.largestRectangleArea([ 1,1 ]))
