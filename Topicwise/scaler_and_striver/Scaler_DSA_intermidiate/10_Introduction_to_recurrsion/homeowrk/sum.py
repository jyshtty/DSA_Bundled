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

def sum(n):
    return 1 if n == 1 else n + sum(n-1)

print(sum(5))
