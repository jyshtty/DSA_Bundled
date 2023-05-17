class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        dict01 = {}
        count = 0
        for i in range(1,A+1):
            dict01[i] = i

        for i in range(1,A+1):
            if i*i in dict01:
                count = count + 1
        return count

if __name__ == "__main__":
    A = 6
    obj =  Solution()
    print(obj.solve(A))