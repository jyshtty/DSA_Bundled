# TC - O(n) + O(n) + O(n) = O(N)
# SC - O(2N)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left_max_array = []
        right_max_array = []
        l, r = 0, len(A) - 1
        max_left = 0
        max_right = 0
        while (l < len(A)):
            max_left = max(max_left, A[l])
            left_max_array.append(max_left)
            l = l+1

            max_right = max(max_right, A[r])
            right_max_array.append(max_right)
            r = r-1

        right_max_array = right_max_array[::-1]

        sum = 0
        for i in range(1, len(A) - 1):
            step = min(left_max_array[i], right_max_array[i])
            sum = sum + step - A[i]
        return sum