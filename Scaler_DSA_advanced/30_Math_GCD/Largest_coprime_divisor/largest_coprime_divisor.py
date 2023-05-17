"""
Problem Description

You are given two positive numbers A and B . You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1


Problem Constraints
1 <= A, B <= 109



Input Format
First argument is an integer A.
Second argument is an integer B.



Output Format
Return an integer maximum value of X as descibed above.



Example Input
Input 1:

 A = 30
 B = 12
Input 2:

 A = 5
 B = 10


Example Output
Output 1:

 5
Output 2:

 1


Example Explanation
Explanation 1:

 All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30).
 The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
Explanation 2:

 1 is the only value such that A%5 == 0 and gcd(1,10) = 1
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self,A,B):
        if B == 0:
            return A
        return self.gcd(B, A%B)

    def cpFact(self, A, B):
        gcd1 = self.gcd(B, A%B)

        while gcd1 != 1:
            A = A// gcd1
            gcd1 = self.gcd(B, A%B)

        if gcd1 == 1:
            return A

if __name__ == '__main__':
    A = 30
    B = 12
    obj = Solution()
    print(obj.cpFact(A, B))

{-5, 5, -2, 2, -8, 4, 7, 1, 8, -7}

index = 10
outofbound = 6

rotate(A, 4, 9)



outofbound = -1
for i in len(range(A)):

    if outofbound > -1:
        if (A[outofbound] < 0 and A[index] > 0) or  (A[outofbound] > 0 and A[index] < 0):
            rotate(A, outofbound, index)
            if (index - outofbound) > 2:
                outofbound +=2
            else:
                outofbound = -1

    if ((index % 2 ) == 0 and A[index] > 0 ) or (index % 2 == 1 and A[index] < 0) :
        outofbound = index

