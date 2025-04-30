from collections import deque
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, arr, k):
        Qi = deque()
        n = len(A)
        ls = []
        for i in range(k):
            while Qi and arr[i] >= arr[Qi[-1]]:
                Qi.pop()
            Qi.append(i);
        for i in range(k, n):
            ls.append(arr[Qi[0]])
            while Qi and Qi[0] <= i - k:
                Qi.popleft()
            while Qi and arr[i] >= arr[Qi[-1]]:
                Qi.pop()
            Qi.append(i)
        ls.append(arr[Qi[0]])
        return ls


# Driver code
if __name__ == "__main__":
    A = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    obj = Solution()
    print(obj.slidingMaximum(A, k))