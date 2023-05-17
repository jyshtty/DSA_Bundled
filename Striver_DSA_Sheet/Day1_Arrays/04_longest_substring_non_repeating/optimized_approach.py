def foo(s):
    l = 0
    r = 0
    maxi = 0
    dict01 = {}
    while r < len(s):
        if s[r] in dict01:
            if l <= dict01[s[r]]:
                l = dict01[s[r]] + 1
        dict01[s[r]] = r
        maxi = max((r - l + 1), maxi)
        r = r + 1
    return maxi
s = "tmmzuxt"
a = "0123456789"
print(foo(s))




