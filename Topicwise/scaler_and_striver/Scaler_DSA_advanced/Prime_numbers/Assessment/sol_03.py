class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        i = 1
        while i*i <= A:
            count = count + 1
            i = i + 1
        return count

if __name__ == "__main__":
    A = 6
    obj =  Solution()
    print(obj.solve(A))