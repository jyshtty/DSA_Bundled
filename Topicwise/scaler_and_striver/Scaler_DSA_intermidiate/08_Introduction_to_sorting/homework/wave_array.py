class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()  # [1,2,3,4]
        ls = [0] * len(A)
        # import pdb; pdb.set_trace()
        for i in range(len(A)):
            try:
                if i % 2 == 0:
                    ls[i] = A[i + 1]
                else:
                    ls[i] = A[i - 1]
            except:
                ls[i] = A[i]
        return ls


if __name__ == "__main__":
    A = [ 5, 1, 3, 2, 4 ] #[2,1,4,3,5]
    obj = Solution()
    print(obj.wave(A))