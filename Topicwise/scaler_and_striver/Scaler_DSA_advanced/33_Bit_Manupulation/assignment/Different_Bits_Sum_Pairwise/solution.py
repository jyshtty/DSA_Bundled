class Solution:
    # @param A : list of integers
    # @return an integer
    def count_number_of_set_bits(self, xor):
        count = 0
        k = 1
        for i in range(32):
            x = xor >> i
            count = count + (x & k)
        return count

    def cntBits(self, A):
        if len(A) == 1:
            return 0
        res = 0
        for i in range(len(A)-1):
            for j in range(i+1,(len(A))):
                xor = A[i] ^  A[j]
                res = res + self.count_number_of_set_bits(xor)
        return res*2

if __name__ == "__main__":
    A = [ 81, 13, 2, 7, 96 ]
    obj = Solution()
    print(obj.cntBits(A))

010

100

110




