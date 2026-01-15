# leetcode 378: Kth Smallest Element in a Sorted Matrix
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Example 1:
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Example 2:
# Input: matrix = [[-5]], k = 1
# Output: -5

# Approach: Heap
# Use a min heap to store the smallest elements from each row.
# Start by pushing the first element of each row into the heap.
# For k-1 times, pop the smallest, and push the next element in that row if exists.
# The kth pop is the answer.
# Time Complexity: O(k log n)
# Space Complexity: O(n)

# Implementation:

# Note - You can't garentee matrix[0][1] is always < matrix[1][0]

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, mat, k):
        n = N = len(mat)
        
        heap = []
        from heapq import heapify, heappop, heappush
        heapify(heap)
        
        for i in range(min(k, n)): # if you have 100 rows and your k is 5, then kth smallest  number will definately be less than k row. so we take range of min(k, n)
            heappush(heap, [mat[i][0], i, 0]) # insert first of all the rows. along with row and column number
        
        while k != 1:
            value, row, col = heappop(heap)
            if col < (len(mat[0])-1):
                heappush(heap, [mat[row][col+1] , row, col+1])
            k = k-1
        
        
        return heap[0][0]
        
