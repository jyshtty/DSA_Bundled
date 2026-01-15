# leetcode 42: Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# https://leetcode.com/problems/trapping-rain-water/
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Approach: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:


# Time complexity - O(N)
# Space Complexity - O(1)

# 1. take 5 variables - left, right, left_max, right_max, and res
# 2. While left <= right
# 3. check if height on the left less than height on right. This is because in prefixmax method we used to calculate water accumulated on top of a block by min(left_max, right_max) - height.
# but here instead of finding min in between prefix max left and prefix max right, whichever is les in between height[left] and height[right] is executed.
# 4. if height[left]  > leftmax, no water is accumulated over.
# so just update leftmax
# 5. Otherwise water is accumalated on height[left]. which is given by ans = left_max - height[left]

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        leftmax = 0
        rightmax = 0

        res = 0

        while left <= right:
            if height[left] <= height[right]: # to make sure we dont have to consider hieght[right] for calculating res
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    res += leftmax - height[left]
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    res += rightmax - height[right]
                right -= 1
        return res

obj = Solution()
print(obj.trap([4,1,2,3]))