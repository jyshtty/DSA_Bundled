class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
		B = A
		sum = 0
		while (B != 0):
			sum = sum + B%10 *10
			B = B//10
        return sum
        # if sum == A:
		# 	return sum
		# else:
		# 	False

if __name__ == "__main__":
    A = 12121
    obj = Solution()
    print(obj.isPalindrome(A))