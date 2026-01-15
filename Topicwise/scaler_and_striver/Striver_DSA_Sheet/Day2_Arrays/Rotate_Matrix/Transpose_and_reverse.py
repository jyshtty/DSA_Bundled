# leetcode 48: Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# https://leetcode.com/problems/rotate-image/
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Approach: Transpose then reverse each row
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Implementation:


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return matrix


if __name__ == "__main__":
    obj = Solution()
    print(obj.rotate([[1,2,3],[4,5,6],[7,8,9]]))