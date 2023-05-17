class Solution:
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low)//2

            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.binary_search([2,4,10,10,10,18,20], 10))