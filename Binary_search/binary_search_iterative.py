class Solution:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return "not found"

if __name__ == "__main__":
    arr = [1,2,3,5,10,25,30,45]
    target = 10
    obj = Solution()
    print(obj.binary_search(arr, target))