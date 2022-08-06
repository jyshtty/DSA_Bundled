class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A, B):
        sum = 0
        prefix_array = [0] * len(A)
        for i in range(len(A)):
            sum = sum + A[i]
            prefix_array[i] = sum
        dict01 = {0:-1}
        for i in range(len(prefix_array)):
            if (prefix_array[i] - B) not in dict01:
                dict01[prefix_array[i]] = i
            else:
                return   A [ (dict01[prefix_array[i] - B] + 1) :i+1]
        return [-1]

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    B = 5
    obj = Solution()
    print(obj.solve(A, B))