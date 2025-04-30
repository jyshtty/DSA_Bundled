class Solution:
    def prefix_sum(self,A, B):
        p = [0] * (B+1)
        sum = 0
        for i in range(1,B+1):
            sum = sum + A[i-1]
            p[i] = sum
        return p

    def sufix_sum(self,A, B):
        s = [0] * (B+1)
        sum = 0
        l = len(A)
        j = 1
        for i in range(l - 1, l-1-B, -1):
            sum = sum + A[i]
            s[j] = sum
            j += 1
        return s

    def solve(self, A, B):
        prefix_sums = self.prefix_sum(A,B)
        sufix_sums = self.sufix_sum(A,B)
        print(prefix_sums,sufix_sums)
        r = len(prefix_sums)-1
        l = 0
        maxi = 0
        for i in range(B+1):
             maxi = max((sufix_sums[l] + prefix_sums[r]),maxi)
             l += 1
             r -= 1
        return maxi

if __name__ == "__main__":
    A = [5, -2, 3, 1, 2]
    B = 3
    obj = Solution()
    print(obj.solve(A,B))
