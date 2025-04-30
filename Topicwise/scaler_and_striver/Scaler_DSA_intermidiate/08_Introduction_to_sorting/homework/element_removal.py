class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cost = 0
        A.sort(reverse = True)
        for i in range(len(A)):
            cost = cost + A[i]*(i+1)
        return cost

if __name__ == '__main__':
    A = [5]
    obj = Solution()
    print(obj.solve(A))