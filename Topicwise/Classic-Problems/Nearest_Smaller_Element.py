# Nearest Smaller Element
# Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
# More formally, G[i] for an element A[i] = an element A[j] such that j is maximum possible AND j < i AND A[j] < A[i]
# Elements for which no smaller element exist, consider the next smaller element as -1.
# Approach: Monotonic Stack
# Use a stack to keep elements in increasing order.
# For each element, pop from stack if top >= current, then the top is the previous smaller.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Implementation:

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        ans = []
        stack = []
        for i in range(0, len(A), 1):
            while stack and stack[-1] >= A[i]:
                stack.pop()
            if stack == []:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(A[i])
        return ans