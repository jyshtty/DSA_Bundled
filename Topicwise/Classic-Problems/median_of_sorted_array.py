class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2) # total length
        half = total // 2 # half length
        
        if len(B) < len(A): # make sure A is smaller array
            A, B = B, A
        
        l, r = 0, len(A) - 1 # binary search on smaller array A
        while True:
            i = (l + r) // 2 # A # partition index
            j = half - i - 2 # B # partition index
        
            Aleft = A[i] if i >= 0 else float("-infinity") # left part of A
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # right part of A
            Bleft = B[j] if j >= 0 else float("-infinity") # left part of B
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") # right part of B
        
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
