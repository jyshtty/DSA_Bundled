"""
Problem Description

Given an array of integers A of size N.

Value of a subarray is defined as BITWISE OR of all elements in it.

Return the sum of Value of all subarrays of A % 109 + 7.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 108



Input Format
The first argument given is the integer array A.



Output Format
Return the sum of Value of all subarrays of A % 109 + 7.



Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [7, 8, 9, 10]


Example Output
Output 1:

 71
Output 2:

 110


Example Explanation
Explanation 1:

 Value([1]) = 1
 Value([1, 2]) = 3
 Value([1, 2, 3]) = 3
 Value([1, 2, 3, 4]) = 7
 Value([1, 2, 3, 4, 5]) = 7
 Value([2]) = 2
 Value([2, 3]) = 3
 Value([2, 3, 4]) = 7
 Value([2, 3, 4, 5]) = 7
 Value([3]) = 3
 Value([3, 4]) = 7
 Value([3, 4, 5]) = 7
 Value([4]) = 4
 Value([4, 5]) = 5
 Value([5]) = 5
 Sum of all these values = 71
Explanation 2:

 Sum of value of all subarray is 110.

"""

class Solution:
    # @param A : list of integers
    # @return an integer

    def bitwise_or_for_all_subarray(self, A):
        sum = 0
        count = 0
        for i in A:
            if i == 0:
                count = count + 1
            else:
                sum = sum + (count * (count+1))/2
                count = 0
        sum = sum + (count * (count + 1)) / 2
        n = len(A)
        total_sum = n*(n+1)/2
        return total_sum - sum

    def solve(self, A):
        matrix = []
        maxi = max(A)
        bin_max = str(bin(maxi)).split('b')[1]
        len_bin_max = len(bin_max)
        for i in range(len_bin_max):
            matrix.append([])

        for i in A:
            binary = str(bin(i)).split('b')[1]
            len_bin = len(binary)
            binary = ('0' * (len_bin_max - len_bin)) + binary

            for i in range(len_bin_max):
                matrix[i].append(int(binary[i]))

        res  = 0
        for i in range(len_bin_max):
            res = res + self.bitwise_or_for_all_subarray(matrix[len_bin_max-i-1]) * (2 ** i)

        return res

if __name__ == "__main__":
    A = [1,2,3,4,5]
    obj = Solution()
    print(obj.solve(A))

    put in a
    tuple,
    for arrived put 0 as first elemnet, 1 for departure.Second element witll be days.then sort array of tuple.increment count when you encounter 1 and decrement 1 when you encounter 0. if count > k return zero.


