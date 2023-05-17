"""
Problem Description

A city is of rectangular shape with the size A * B meters. On the occasion of the city's anniversary, a decision was taken to pave the city with square granite flagstones. Each flagstone is of the size C * C. What is the least number of flagstones needed to pave the city?

NOTE: It's allowed to cover the surface larger than the city, but the city has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the city.



Problem Constraints
1 <= A <= 109

1 <= B <= 109

1 <= C <= 109



Input Format
First argument is an integer A as per the question.

Second argument is an integer B as per the question.

Third argument is an integer C as per the question.



Output Format
Return an integer showing least number of flagstones needed.



Example Input
Input 1:

A=6, B=6, C=4


Example Output
Output 1:

4


Example Explanation
Explanation 1:

If we use 4 flagstones(2 rows and 2 columns) then it will cover the whole city.



You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        a = A/2
        b = B/2
        i = 0
        j = 0
        c = C / 2
        while c < a:
            c = C / 2
            i = i + 1
            c = c * i
        c = C / 2
        while c < b:
            c = C / 2
            j = j + 1
            c = c * j

        if i+j ==0:
            return 1
        if i == 0:
            i = 1
        if j == 0:
            j = 1
        return i * j

if __name__ == "__main__":
    A= 87
    B= 5
    C= 39
    obj = Solution()
    print(obj.solve(A,B,C))

