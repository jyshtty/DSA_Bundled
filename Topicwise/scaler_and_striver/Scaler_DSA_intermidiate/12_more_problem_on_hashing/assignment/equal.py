"""
Equal
Problem Description

Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P,Q,R & S are integers values in the array

Expected time complexity O(N2)

NOTE:

1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices in the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 if:
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
If no solution is possible, return an empty list.



Problem Constraints
1 <= N <= 1000

0 <= A[i] <= 1000



Input Format
Single argument which is an integer array A of size N.



Output Format
Return an array of size 4 which indexes of values P,Q,R and S.



Example Input
Input 1:

 A = [3, 4, 7, 1, 2, 9, 8]
Input 2:

 A = [2, 5, 1, 6]


Example Output
Output 1:

 [0, 2, 3, 5]
Output 2:

 [0, 1, 2, 3]


Example Explanation
Explanation 1:

 A[0] + A[2] = A[3] + A[5]
 Note: indexes returned should be 0-based.
Explanation 2:

 A[0] + A[1] = A[2] + A[3]
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        dict01 = {}
        ans = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                sum = A[i] + A[j]
                if sum not in dict01:
                    dict01[sum] = i,j
                else:
                    k,l = dict01[sum]
                    if k != i and k != j and l != i and l != j:
                        if ans == 0:
                            ans = [k,l,i,j]
                        else:
                            if ans[0] < k:
                                continue
                            elif ans[0] > k:
                                ans = [k,l,i,j]
                                continue
                            else:
                                if ans[1] < l:
                                    continue
                                elif ans[1] > l:
                                    ans = [k, l, i, j]
                                    continue
                                else:
                                    if ans[2] < i:
                                        continue
                                    elif ans[2] > i:
                                        ans = [k, l, i, j]
                                        continue
                                    else:
                                        if ans[3] < j:
                                            continue
                                        elif ans[3] > j:
                                            ans = [k, l, i, j]
                                            continue
                                        else:
                                            continue
                    else:
                        continue
        return ans



if __name__ == "__main__":
    A = [2, 5, 1, 6]
    obj = Solution()
    print(obj.equal(A))