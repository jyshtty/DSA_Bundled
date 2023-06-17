class Solution:
    def search(self, nums, target):

        high = len(nums) - 1
        low = 0

        if high == low and target == nums[low]:
            return low

        while high >= low:
            mid = low + (high - low) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    obj = Solution()
    print(obj.search(nums, target))
