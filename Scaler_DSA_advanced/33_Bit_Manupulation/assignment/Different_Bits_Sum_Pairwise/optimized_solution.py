class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        intermidiate_result = 0
        if len(A) == 1:
            return 0
        for j in range(32):
            count_of_one = 0
            count_of_zero = 0
            for i in A:
                x = i >> j
                if (x & 1):
                    count_of_one  += 1
                else:
                    count_of_zero  += 1
            intermidiate_result = intermidiate_result + (count_of_one * count_of_zero)
        return intermidiate_result * 2

if __name__ == "__main__":
    A = [ 81, 13, 2, 7, 96 ]
    obj = Solution()
    print(obj.cntBits(A))

10

x = 15

x = x % 10

x = 5














