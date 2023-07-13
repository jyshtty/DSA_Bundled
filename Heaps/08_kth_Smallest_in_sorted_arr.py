# Given a sorted matrix of integers A of size N x M and an integer B.
#
# Each of the rows and columns of matrix A is sorted in ascending order, find the Bth smallest element in the matrix.
#
# NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, mat, k):
        n = N = len(mat)

        heap = []
        from heapq import heapify, heappop, heappush
        heapify(heap)

        for i in range(min(k,
                           n)):  # if you have 100 rows and your k is 5, then kth smallest  number will definately be less than k row. so we take range of min(k, n)
            heappush(heap, [mat[i][0], i,
                            0])  # insert first of all the rows. along with row and column number. The idea is all the number comes on right of a single row is always greater thanthe number before it.

        while k != 1:
            value, row, col = heappop(heap)
            if col < (len(mat[0]) - 1):
                heappush(heap, [mat[row][col + 1], row, col + 1])
            k = k - 1

        return heap[0][0]

