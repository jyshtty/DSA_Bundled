s = "abcaabcdba"
s1 = "abcdefghijkbb"

def foo(s):
    a = set()
    l = 0
    r = 0
    maxi = 0
    while(r<len(s)):
        if s[r] not in a:
            a.add(s[r])
            maxi = max((r-l + 1), maxi)
            r = r + 1
        else:
            a.remove(s[l])
            l = l + 1
    return maxi

s = "abcaabcdba"
print(foo(s))











