# Leetcode 135: Candy
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# - Each child must have at least one candy.
# - Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
# https://leetcode.com/problems/candy/
# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Approach: Use two arrays to keep track of candies from left and right, then take max.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Implementation:

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        left = []
        left.append(1)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)

        right = []
        right.append(1)
        for i in range(len(A) - 2, -1, -1):
            if A[i + 1] < A[i]:
                right.append(right[-1] + 1)
            else:
                right.append(1)

        right = right[::-1]

        ans = []

        for i in range(len(left)):
            ans.append(max(left[i], right[i]))

        return ans

A = [1, 2]
obj = Solution()
print(obj.candy(A))
