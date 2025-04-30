def isPalindrome(str, l, r):
    while(l<r):
        if str[l] != str[r]:
            return 0
        else:
            return isPalindrome(str, l + 1, r- 1)
    return 1




class Solution:
    def solve(self, str):
        l = 0
        r = len(str) - 1

        return isPalindrome(str, l, r)

obj = Solution()
print(obj.solve('malayaam'))