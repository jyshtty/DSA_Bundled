class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        lastseen = {}
        maxlen = 0
        while r < len(s):
            if s[r] in lastseen:
                if l <= lastseen[s[r]]:
                    l = lastseen[s[r]] + 1
                lastseen[s[r]] = r
                le = r - l + 1
                maxlen = max(maxlen, le)
            else:
                lastseen[s[r]] = r
                le = r-l+1
                maxlen = max(maxlen, le)
            r += 1
        return maxlen
A = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(A))
