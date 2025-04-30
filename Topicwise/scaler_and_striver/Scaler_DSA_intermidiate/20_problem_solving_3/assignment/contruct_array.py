"""
Problem Description

Simba has an integer array of length A. Despite having insisted alot, He is not ready to reveal the array to his friend Expert. But now, he is ready to reveal some hints about the array and challenges Expert to find the values of his hidden array. The hints revealed are as follows:

The array is sorted by values in ascending order.
All the elements in the array are distinct and positive (greater than 0).
The array contains two elements B and C such that B < C.
Difference between all adjacent (consecutive) elements are equal.
Among all the arrays satisfying the above conditions, his array has the minimum possible maximum element value.
If there are multiple possible arrays, his array will have minimum possible minimum element value.
Can you help Expert to construct such an array and surprise Simba?



Problem Constraints
2 <= A <= 50

1 <= B < C <= 50



Input Format
First argument is an integer A.

Second argument is an integer B.

Third argument is an integer C.



Output Format
Return a sorted integer array having length N, denoting Simba's Secret Array.



Example Input
Input 1:

 A = 5
 B = 20
 C = 50
Input 2:

 A = 2
 B = 2
 C = 3


Example Output
Output 1:

 [10, 20, 30, 40, 50]
Output 2:

 [2, 3]


Example Explanation
Explanation 1:

 Sorted array = [10, 20, 30, 40, 50] satisfies all the conditions having maximum value = 50 minimum possible.
 Other arrays such as [20, 30, 40, 50, 60] having max value = 60 or [20, 50, 80, 120] having max value = 120, also satisfy conditions but their maximum value is not minimum possible(As minimum possible max value is 50).
Explanation 2:

 As the array has only 2 elements, [2, 3] is the only possible candidate.
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a list of integers

    # def compute_hcf(self, x, y):
    #     while (y):
    #         x, y = y, x % y
    #     return x
    #
    def solve(self, A, B, C):
        d = C - B
        x = 0 # number of elements between B & C
        result = []
        dict01 = {}
        while(x<= A-2):

            if(d % (x+1) == 0 ):
                diff = d/(x+1)
                elements_btw_B_C = x
                result = [B]

                if elements_btw_B_C >= 1:
                    next_element = B
                    for i in range(elements_btw_B_C):
                        next_element = next_element + diff
                        result.append(next_element)
                result.append(C)
                if elements_btw_B_C == (A - 2):
                    return result

                left_result = right_result = []

                possible_left_elements =  (B-1)//diff # number of element towards left of B
                if possible_left_elements>0 :
                    left_elements = min((A-2) - elements_btw_B_C,possible_left_elements)
                else:
                    left_elements = 0
                if left_elements > 0:
                    element = B - diff
                    left_result = [element]

                    for i in range(left_elements-1):
                        element = element - diff
                        left_result.append(element)
                    left_result = left_result[::-1]

                right_elements = (A - 2) - elements_btw_B_C - left_elements # number of element towards
                if right_elements > 0:
                    right_result = []
                    element = C + diff
                    right_result = [element]
                    for i in range(right_elements-1):
                        element = element + diff
                        right_result.append(element)


            if left_elements == 0:
                dict01[x] = result + right_result
            elif right_elements == 0:
                dict01[x] = left_result + result
            else:
                dict01[x] = left_result + result + right_result

            x = x + 1

        # return dict01
        array = [float('inf')] * (A-1)
        for i in dict01:
            if dict01[i][-1] < array[-1]:
                array = dict01[i]
            elif dict01[i][-1] < array[-1]:
                if dict01[i][0] < array[0]:
                    array = dict01[i]
        return array

if __name__ == "__main__":
    A = 2
    B = 2
    C = 3
    obj = Solution()
    print(obj.solve(A,B,C))

