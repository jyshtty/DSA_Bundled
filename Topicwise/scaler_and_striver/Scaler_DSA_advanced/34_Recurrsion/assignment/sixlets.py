class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        global n
        n = len(A)
        self.count = 0
        curr = [-1 for i in range(len(A))]
        self.generate(curr)
        return self.count

    def generate(self, curr, index=0):
        if index == n:
            sum = 0
            if curr.count(1) == B:
                for i in range(len(curr)):
                    if curr[i] == 1:
                        sum = sum + A[i]
                if sum <= 1000:
                    self.count += 1
            return
        curr[index] = 0
        self.generate(curr, index+1)
        curr[index] = 1
        self.generate(curr, index+1)

if __name__ == "__main__":
    A = [ 508, 503, 412, 895, 256, 89, 245, 567, 9, 123 ]
    B = 5
    obj = Solution()
    print(obj.solve(A, B))