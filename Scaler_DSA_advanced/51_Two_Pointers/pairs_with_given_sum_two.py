class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    import operator as op
    from functools import reduce

    # def ncr(self, n, r):
    #     r = min(r, n - r)
    #     numer = reduce(op.mul, range(n, n - r, -1), 1)
    #     denom = reduce(op.mul, range(1, r + 1), 1)
    #     return numer // denom  # or / in Python 2

    def solve(self, A, B):
        hash_map = {}
        count = 0
        for i in A:
            if i in hash_map:
                count = count + hash_map[i]
                if hash_map.get(B - i):
                    hash_map[B - i] += 1
                else:
                    hash_map[B - i] = 1
            else:
                if hash_map.get(B - i):
                    hash_map[B - i] += 1
                else:
                    hash_map[B - i] = 1
        return count

if __name__ == "__main__":
    A =  [ 2,2,3,3]
    B = 5
    obj = Solution()
    print(obj.solve(A, B))