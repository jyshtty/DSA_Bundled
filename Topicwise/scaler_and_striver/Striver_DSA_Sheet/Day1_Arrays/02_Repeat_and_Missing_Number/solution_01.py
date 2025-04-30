"""
Repeat and Missing Number
https://www.youtube.com/watch?v=5nMGY4VUoRY&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=3  (Problem link in description)
"""

def foo1(A):
    n = len(A)
    sum1 = (n * (n+1))//2
    sum_a = sum(A)
    ls_sqare = [i*i for i in A]
    sum_square = sum(ls_sqare)
    sum_of_square = (n*(2*n+1) * (n+1))//6
    ans = sum_of_square - sum_square
    ans2 = sum1 - sum_a # x - y
    xplusy = ans//ans2
    missing_number = (ans2 + xplusy)//2
    repeating_number = (missing_number - ans2)
    print(missing_number, repeating_number)

A = [4,3,6,2,1,1]
foo(A)