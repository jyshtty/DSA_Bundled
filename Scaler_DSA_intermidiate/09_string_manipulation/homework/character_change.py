class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        count = 0
        dict01 = {}
        for i in A:
            if i in dict01:
                dict01[i] += 1
            else:
                dict01[i] = 1
        count = sorted(dict01.values())

        answer = len(count) # number of distinct element

        for i in range(len(count)-1): # -1 because atleast we have to return 1 distinct
            if count[i] <= B:
               B = B - count[i]
               answer -= 1
            else:
                break
        return answer



if __name__ == "__main__":
    obj = Solution()
    print(obj.solve("abcabbccd", 3))