"""
You have given a string A having Uppercase English letters.

You have to find that how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
"""

def find_subsequence(string):
    count_a = count = 0
    for i in string:
        if i == 'A':
            count_a += 1
        if i == 'G':
            count = count_a + count
    return count

A = "ABCGAG"
print(find_subsequence(A))
