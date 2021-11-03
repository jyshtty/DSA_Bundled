from math import factorial
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        res = 0
        s = sorted(A)
        lna = len(A)
        e = 1
        vis = set()
        for i in A:
            c = 0
            for j in s:
                if j in vis:
                    continue
                if j >= i:
                    vis.add(j)
                    break
                c += 1
            res += c * factorial(lna - e)
            e += 1
        return (res + 1) % 1000003

if __name__ == "__main__":
    A = "BCAD"
    obj = Solution()
    print(obj.findRank(A))