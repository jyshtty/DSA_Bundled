class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return (B-A+1) - (B//3 - (A-1)//3)

if __name__ == "__main__":
    A = 6
    B = 20
    obj = Solution()
    print(obj.solve(A,B))