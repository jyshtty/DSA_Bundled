class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, B, C):
        if C == 0:
            return B
        return self.gcd(C, B % C)

    def solve(self, A, B, C):
        gcd1 = self.gcd(B, C)
        lcm = (B * C) / gcd1

        if lcm > A:
            return 0
        return A/lcm

if __name__ == "__main__":
    A= 81991
    B= 2549
    C= 7
    obj = Solution()
    print(obj.solve(A,B,C))