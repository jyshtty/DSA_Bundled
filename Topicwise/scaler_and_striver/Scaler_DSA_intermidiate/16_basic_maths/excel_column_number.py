class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		n = len(A)
		A = A.lower()
		sum = 0
		for i in range(len(A)):
			sum = sum + (26 ** i) * (ord(A[n-1-i]) - 96)
		return sum

if __name__  == '__main__' :
	obj = Solution()
	print(obj.titleToNumber('ABCD'))