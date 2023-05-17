def next_permutation(a):
    s = str(a)
    r = 0
    while r < len(s)-1:
        if s[r] < s[r+1]:
            break_point = s[r+1]
            index1 = r+1
            c = 10
            break
        r = r + 1
    else:
        return ("It is the last number in permutation")
    r = len(s)-1
    while r > -1:
        if s[r] >= break_point:
            index2 = r
            break
        r = r -1

    ls = []
    ls[:0] = s

    ls[index1], ls[index2] = ls[index2], ls[index1]
    res = ''
    resultant = res.join(ls)
    return resultant

a = 321

print(next_permutation(a))



