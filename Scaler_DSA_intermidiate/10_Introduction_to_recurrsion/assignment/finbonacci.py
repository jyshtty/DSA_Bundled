class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, n):
        return 0 if n == 0 elif n == 1 else self.findAthFibonacci(n-1) + self.findAthFibonacci(n-2)

a = Solution()
print(a.findAthFibonacci(4))

# def findAthFibonacci(n):
#     return 1 if n < 2 else findAthFibonacci(n - 1) + findAthFibonacci(n - 2)
#
# print(findAthFibonacci(5))

