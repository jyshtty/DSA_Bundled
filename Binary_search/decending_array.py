class Binary_Search:
    def solve(self, arr, target):
        high = 0
        low = len(arr)-1

        while high <= low:
            mid = high + (low - high)//2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = low-1
            else:
                high = high + 1

        return "Not found"

if __name__ == "__main__":
    obj = Binary_Search()
    print(obj.solve([49, 40, 30, 25, 19, 9, 4, 2], 40))