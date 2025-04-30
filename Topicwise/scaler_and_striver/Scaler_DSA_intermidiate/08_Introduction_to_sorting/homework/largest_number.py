from itertools import permutations
class Solution:
    def largestNumber(self, l):
        # lst = []
        # for i in permutations(l, len(l)):
        #     lst.append("".join(map(str,i)))
        # return max(lst)
        for i in range(len(l)-1):
            mini =
            for j in range(i+1,len(l)-1):


if __name__ == '__main__':
    A = [3, 30, 34, 5, 9]
    obj = Solution()
    print(obj.largestNumber(A))