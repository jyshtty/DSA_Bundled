class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []

        def generate(index, temp):
            if index == len(nums):
                ans.append(temp)
                return
            generate(index + 1, temp + [nums[index]])
            generate(index + 1, temp)
        generate(0, temp)
        return sorted(ans)


# By not passing temp as arguement
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []

        def generate(index):
            if index == len(nums):
                
                #You do this coz of shallow copy                 
                new = []
                for i in temp:
                    new.append(i)
                ans.append(new)
                
                return
            temp.append(nums[index])
            generate(index + 1)
            temp.pop()
            generate(index + 1)

        generate(0)

        return sorted(ans)

if __name__ == "__main__":
    nums = [1,2,3]
    obj = Solution()
    print(obj.subsets(nums))
