class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        A = list(A)
        candidate = None
        count = 0

        # Phase 1: Find candidate
        for num in A:
            if count == 0:
                candidate = num # potential majority element
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Phase 2: Verify candidate
        if A.count(candidate) > len(A) // 2:
            return candidate

        return -1
