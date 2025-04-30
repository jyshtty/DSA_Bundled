"""
Closest MinMax
Problem Description

Given an array A. Find the size of the smallest subarray such that it contains atleast one occurrence of the maximum value of the array

and atleast one occurrence of the minimum value of the array.



Problem Constraints
1 <= |A| <= 2000



Input Format
First and only argument is vector A



Output Format
Return the length of the smallest subarray which has atleast one occurrence of minimum and maximum element of the array



Example Input
Input 1:

A = [1, 3]
Input 2:

A = [2]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 Only choice is to take both elements.
Explanation 2:

 Take the whole array.
"""

def closest_minmax(arr):
    latest_min = latest_max = -1
    ans = len(arr)
    mini = min(arr)
    maxi = max(arr)
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == mini:
            latest_min = i
            if latest_max != -1:
                ans = min(ans, latest_max - latest_min + 1)
        if arr[i] == maxi:
            latest_max = i
            if latest_min != -1:
                ans = min(ans, latest_min - latest_max + 1)
    return ans

A = [1,3]
print(closest_minmax(A))



