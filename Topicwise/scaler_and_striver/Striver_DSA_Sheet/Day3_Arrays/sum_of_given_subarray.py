# Given an array A of integers and an integer B, find and return the first continuous subarray which adds to B.
# If the answer does not exist return an array with a single element -1.
class Solution:
    def solve(self, A, B):
        prefix_map = {0: -1}
        curr_sum = 0

        for i in range(len(A)):
            curr_sum += A[i]

            if curr_sum - B in prefix_map:
                return A[prefix_map[curr_sum - B] + 1 : i + 1]

            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i

        return [-1]


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 5
    obj = Solution()
    print(obj.solve(A, B))