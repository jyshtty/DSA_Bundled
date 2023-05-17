# Approach1 - Easy Solution


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[0] for i in range(numRows)]
        for i in range(len(ans)):
            ans[i] = ans[i] * (i + 1)
            ans[i][0] = 1
            ans[i][i] = 1
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans

if __name__ == "__main__":
    obj = Solution()
    print(obj.generate(5))