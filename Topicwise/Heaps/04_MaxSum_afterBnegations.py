# HINT
# do heappop
# if
#     negative, make positive and heappush
# else:
#     B = B%2 # which will give 1 or 0. if 1 make smallest number as -ve and add it. else come out of loop.
#     # we do mod2 because even number of times we can make -ve and +ve. which keeps the +ve number as it is.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        from heapq import heapify, heappop, heappush

        heapify(A)
        while B:
            a = heappop(A)
            if a < 0:
                B -= 1
                heappush(A, -1 * a)
            else:
                B = B % 2
                heappush(A, a)
                break

        if B == 1:
            return sum(A) - (2 * a)
        else:
            return sum(A)

if __name__ == "__main__":
    A = [24, -68, -29, -9, 84]
    B = 4
    obj = Solution()
    print(obj.solve(A, B))










