"""
Problem Description

Given an array of integers A of size, N. Minimize the absolute difference between the maximum and minimum element of the array.

You can perform two types of operations at most B times in total to change the values in the array.
Multiple operations can be performed on the same element.

Increment : A[i] -> A[i] + 1.

Decrement : A[i] -> A[i] - 1.

Return the minimum difference possible.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 106

1 <= B <= 109



Input Format
First argument is an integer array A.
Second argument is an integer B which represents the maximum number of operations that can be performed.



Output Format
Return an integer denoting the minimum difference.



Example Input
Input 1:

 A = [2, 6, 3, 9, 8]
 B = 3
Input 2:

 A = [4, 6, 3, 1, 4]
 B = 5


Example Output
Output 1:

 5
Output 2:

 1


Example Explanation
Explanation 1:

 We can apply the atmost 3 operations in the following sequence.
 Initial array => [2, 6, 3, 9, 8].
   Decrement 9 => [2, 6, 3, 8, 8].
   Increment 2 => [3, 6, 3, 8, 8].
   Increment 3 => [3, 6, 4, 8, 8].
 Max = 8. Min = 3.
 Therefore, abs|Max - Min| = |8 - 3| = 5.
Explanation 2:

 We can apply the atmost 5 operations in the following sequence.
 Initial array => [4, 6, 3, 1, 4].
   Increment 1 => [4, 6, 3, 2, 4].
   Decrement 6 => [4, 5, 3, 2, 4].
   Increment 2 => [4, 5, 3, 3, 4].
   Decrement 5 => [4, 4, 3, 3, 4].
   Increment 3 => [4, 4, 4, 3, 4].
 Max = 4. Min = 3.
 Therefore, abs|Max - Min| = |4 - 3| = 1.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def find_min_max(self, A):
        mini = float('inf')
        maxi = -float('inf')
        dict01 = {}

        for i in A:
            if i > maxi:
                maxi = i
            if i < mini:
                mini = i
            if i in dict01:
                dict01[i] += 1
            else:
                dict01[i] = 1
        return maxi, mini, dict01

    def solve(self, A, B):
        maxi, mini, dict01 = self.find_min_max(A)

        while (B != 0 and mini < maxi):

            if maxi == mini:
                return 0
            elif dict01[mini] < dict01[maxi]:
                if B < dict01[mini]:
                    break
                else:
                    temp = dict01[mini] + dict01.get(mini+1, 0)
                    dict01[mini+1] = temp
                    B = B - dict01[mini]
                    mini = mini+1
            else:
                if B < dict01[maxi]:
                    break
                else:
                    temp = dict01[maxi] + dict01.get(maxi-1, 0)
                    dict01[maxi-1] = temp
                    B = B - dict01[maxi]
                    maxi = maxi-1
        return maxi - mini


if __name__ == "__main__":
    A = [2, 6, 3, 9, 8]
    B = 3
    obj = Solution()
    print(obj.solve(A, B))
