def lengthOfLongestSubstring(s):
    l = 0
    r = 1
    dict01 = {s[0]:0}
    maxi = 1
    while r < len(s):
        if s[r] not in dict01:
            dict01[s[r]] = r
            maxi = max((r-l+1), maxi)
        else:
            if l < dict01[s[r]]:
                l = dict01[s[r]] + 1
            dict01[s[r]] = r
        r += 1
    return maxi


s = "bbbbb"
a = "0123456789"
print(lengthOfLongestSubstring(s))