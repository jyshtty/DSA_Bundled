from collections import deque
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if len(A) < 3: return 0
        stack = deque()
        i = 0
        ans = 0
        for i in range(len(A)):
            while len(stack) != 0 and A[i] > A[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break
                distance = i - stack[-1] -1
                bounded_bars_height = min(A[i], A[stack[-1]]) - A[top]
                ans += distance * bounded_bars_height
            stack.append(i)
        return ans

if __name__ == "__main__":
    A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
    obj = Solution()
    print(obj.trap(A))