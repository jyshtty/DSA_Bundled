def kmp_substring_match(A, search):
    for i in range(len(A)-len(search)+1):
        l = 0
        r = i
        while (l < len(search)):
            if A[r] != search[l]:
                break
            else:
                r += 1
                l += 1
        else:
            return "found"
    return "not found"

A = "abcbcglx"
search = "bcglx"
print(kmp_substring_match(A,search))