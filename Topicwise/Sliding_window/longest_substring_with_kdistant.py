class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        l = 0
        hm = {}
        max_len = 0

        for r in range(len(s)):

            hm[s[r]] = hm.get(s[r], 0) + 1

            while len(hm) > k:
                hm[s[l]] -= 1
                
                if hm[s[l]] == 0:
                    del hm[s[l]]
                    
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
