"""
Problem Description

Given an array of integers A of size N containing GCD of every possible pair of elements of another array.

Find and return the original numbers which are used to calculate the GCD array in any order. For example, if original numbers are {2, 8, 10} then the given array will be {2, 2, 2, 2, 8, 2, 2, 2, 10}.



Problem Constraints
1 <= N <= 10000

1 <= A[i] <= 109



Input Format
The first and only argument given is the integer array A.



Output Format
Find and return the original numbers which are used to calculate the GCD array in any order.



Example Input
Input 1:

 A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
Input 2:

 A = [5, 5, 5, 15]


Example Output
Output 1:

 [2, 8, 10]
Output 2:

 [5, 15]


Example Explanation
Explanation 1:

 Initially, array A = [2, 2, 2, 2, 8, 2, 2, 2, 10].
 2 is the gcd between 2 and 8, 2 and 10.
 8 and 10 are the gcds pair with itself.
 Therefore, [2, 8, 10] is the original array.
Explanation 2:

 Initially, array A = [5, 5, 5, 15].
 5 is the gcd between 5 and 15.
 15 is the gcds pair with itself.
 Therefore, [5, 15] is the original array.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def gcd(self, A, B):
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def make_freq_array(self, arr):
        dict = {}
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        return dict

    def solve(self, arr):
        if len(arr) < 2:
            return arr
        arr.sort()
        output_array = []
        output_array.append(arr.pop())
        output_array.append(arr.pop())
        freq_arr = self.make_freq_array(arr)
        while freq_arr:
            for i in range(len(output_array) - 1):
                j = output_array[-1]
                gcd_new = self.gcd(output_array[i], j)
                freq_arr[gcd_new] -= 2
                if freq_arr[gcd_new] == 0:
                    del freq_arr[gcd_new]
            if freq_arr:
                output_array.append(max(freq_arr))
                freq_arr[max(freq_arr)] -= 1
                if freq_arr[max(freq_arr)] == 0:
                    del freq_arr[max(freq_arr)]
        output_array.sort()
        return output_array

if __name__ == '__main__':
    arr = [ 1, 31, 1, 1, 1, 1, 14, 2, 1, 1, 1, 2, 22, 1, 11, 1, 1, 1, 1, 23, 1, 1, 11, 1, 11 ]
    obj = Solution()
    print(obj.solve(arr))