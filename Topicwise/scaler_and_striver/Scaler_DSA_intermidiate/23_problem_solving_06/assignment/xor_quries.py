class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        prefix_sum = [0]
        for i in range(len(A)):
            if A[i] == 1:
                prefix_sum.append(prefix_sum[i])
            else:
                prefix_sum.append(prefix_sum[i] + 1)
        # print(prefix_sum)
        ans = []
        for query in B:
            left = query[0]
            right = query[1]
            count_0 = prefix_sum[right] - prefix_sum[left - 1]
            xor = 0 if (right - left + 1 - count_0) % 2 == 0 else 1
            ans.append([xor, count_0])
        return ans
