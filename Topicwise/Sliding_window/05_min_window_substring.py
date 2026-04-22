from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""
        
        need = Counter(t)
        window = defaultdict(int)
        
        required = len(need)
        formed = 0
        
        l = 0
        min_len = float("inf")
        ans = ""
        
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            while formed == required:
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]
                
                left_char = s[l]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                l += 1
        
        return ans