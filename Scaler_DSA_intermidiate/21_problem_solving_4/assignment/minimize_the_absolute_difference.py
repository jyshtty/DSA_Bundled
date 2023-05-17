"""
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        a = b = c = 0
        previous_min = float('inf')
        iterate_till_a = iterate_till_b = iterate_till_c = ''
        if A[-1] <= B[-1]:
            if A[-1] <= C[-1]:
                iterate_till_a = len(A)
            else:
                iterate_till_c = len(C)
        else:
            if B[-1] <= C[-1]:
                iterate_till_b = len(B)
            else:
                iterate_till_c = len(C)

        if iterate_till_a:
            while(a <= iterate_till_a):
                curr_min = min(min(A[a], B[b], C[c]), previous_min)
                if curr_min == A[a]:
                    a = a + 1
                elif curr_min == B[b]:
                    b = b + 1
                else:
                    c = c + 1
        if iterate_till_b:
            while (b <= iterate_till_b):
                curr_min = min(min(A[a], B[b], C[c]), previous_min)
                if curr_min == A[a]:
                    a = a + 1
                elif curr_min == B[b]:
                    b = b + 1
                else:
                    c = c + 1
                previous_min = curr_min
        if iterate_till_c:
            while(c < iterate_till_c):
                curr_min = max(min(A[a], B[b], C[c]), previous_min)
                if curr_min == A[a]:
                    a = a + 1
                elif curr_min == B[b]:
                    b = b + 1
                else:
                    c = c + 1
                previous_min = curr_min

        return a,b,c

if __name__ == "__main__":
    A= [1, 4, 5, 8, 10]
    B= [6, 9, 15]
    C= [2, 3, 6, 6]
    obj = Solution()
    print(obj.solve(A,B,C))

