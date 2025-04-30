"""
Sum of Digits!
Problem Description

Given a number A, we need to find sum of its digits using recursion.



Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the sum of digits of the number A.
"""

def sum1(A):
    n = len(str(A))
    # return A%10 if n == 1 else A//(10**(n-1)) + sum1(A % (10**(n-1)))
    return A if n == 1 else A%10 + sum1(A//10)


print(sum1(123))
