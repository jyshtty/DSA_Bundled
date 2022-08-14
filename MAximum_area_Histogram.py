class Solution:
    # @param A : list of integers
    # @return an integer
    def smallestToLeft(self, A):
        psedoindex = -1
        stack = []
        left = []
        for i in range(len(A)):
            while stack and stack[-1][0] >= A[i]:
                stack.pop()
            if not stack:
                left.append(psedoindex)
            else:
                left.append(stack[-1][1])
            stack.append([A[i], i])
        return left

    def smallestToRight(self, A):
        pseudo_index = len(A)
        stack = []
        right = []

        for i in range(len(A) - 1, -1, -1):
            while stack and stack[-1][0] >= A[i]:
                stack.pop()
            if not stack:
                right.append(pseudo_index)
            else:
                right.append(stack[-1][1])
            stack.append([A[i], i])
        return right[::-1]

    def largestRectangleArea(self, A):
        left = self.smallestToLeft(A)
        right = self.smallestToRight(A)

        width = []
        for i in range(len(left)):
            width.append(right[i] - left[i] - 1)
        area = []

        for i in range(len(width)):
            area.append(width[i] * A[i])
        print(A)
        print(left)
        print(right)
        print(width)
        print(area)
        return max(area)

obj = Solution()
print(obj.largestRectangleArea([ 1,1 ]))
