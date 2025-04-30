class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majority_element = A[0]
        count = 1
        n = len(A)
        for i in range(1, len(A)):
            if A[i] == majority_element:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority_element = A[i + 1]
        if count > n / 2:
            return majority_element
        if count > 0:
            if (A.count(majority_element)) > (n/2):
                return majority_element

if __name__ == "__main__":
    A = [ 2, 1, 1 ]
    obj = Solution()
    print(obj.majorityElement(A))








