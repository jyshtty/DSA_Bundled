"""
Pattern Printing -2
Problem Description

Print a Pattern According to The Given Value of A.

Example: For A = 3 pattern looks like:

    1
  2 1
3 2 1


Problem Constraints
1 <= A <= 1000


Input Format
First and only argument is an integer denoting A.



Output Format
Return a two-dimensional array where each row in the returned array represents a row in the pattern.



Example Input
Input 1:

 A = 3
Input 2:

 A = 4


Example Output
Output :1

 [
   [0, 0, 1]
   [0, 2, 1]
   [3, 2, 1]
 ]
Output 2:

 [
   [0, 0, 0, 1]
   [0, 0, 2, 1]
   [0, 3, 2, 1]
   [4, 3, 2, 1]
 ]

"""

def pattern_printing(n):
    ls = [[0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        j = n-1
        for val in range(1,i+2):
            ls[i][j] = val
            j = j-1
    return ls

print(pattern_printing(5))

