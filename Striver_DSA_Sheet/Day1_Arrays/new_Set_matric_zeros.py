#Approach 1
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        return matrix


#APproach 2 - Not working - Solution available in leetcode
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = [0] * len(matrix)
        col = [0] * len(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][0] == 0 or matrix[0][j] == 0) and matrix[i][j]:
                    matrix[i][j] = "0"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
        return matrix

if __name__ == "__main__":
    matrix = [[1,0]]
    obj = Solution()
    print(obj.setZeroes(matrix))
    print("[[1, 0, 1], [0, 0, 0], [1, 0, 1]]")
