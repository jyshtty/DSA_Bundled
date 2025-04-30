"""
Problem Description

Find the intersection of two sorted arrays. OR in other words, Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example:

Input:
    A: [1 2 3 3 4 5 6]
    B: [3 3 5]

Output: [3 3 5]

Input:
    A: [1 2 3 3 4 5 6]
    B: [3 5]

Output: [3 5]
NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.

You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        ls = []
        a = 0
        b = 0
        while(a < len(A) and b < len(B)):
            if A[a] == B[b]:
                ls.append(A[a])
                a +=1
                b +=1
            elif A[a] < B[b]:
                a += 1
            else:
                b += 1
        return ls

if __name__ == "__main__":
    A= [1 ,2, 3, 3, 4, 5, 6]
    B= [3, 3, 5]
    obj = Solution()
    print(obj.intersect(A,B))


