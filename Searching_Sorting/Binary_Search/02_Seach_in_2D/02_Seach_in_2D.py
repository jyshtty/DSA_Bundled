# Divide and mod both should be done by column

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        while high >= low:
            mid = (high + low) // 2
            elem = matrix[mid // n][mid % n]

            if target == elem:
                return True
            elif elem > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.searchMatrix([[1,3]], 3))

