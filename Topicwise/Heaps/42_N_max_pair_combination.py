class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    from heapq import heapify, heappush, heappop
    def solve(self, A, B):
        hp = []
        from heapq import heapify, heappush, heappop
        heapify(hp)

        for i in A:
            for j in B:
                sum = i + j
                if len(hp) < len(A):
                    heappush(hp, sum)
                else:
                    heappush(hp, sum)
                    heappop(hp)

        for i in range(len(hp)):
            hp[i] = -1 * hp[i]

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heap_sort(arr):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n - 1, 0, -1):
                arr[0], arr[i] = arr[i], arr[0]
                heapify(arr, i, 0)

        heap_sort(hp)

        for i in range(len(hp)):
            hp[i] = -1 * hp[i]

        return hp


if __name__ == "__main__":
    A = [36,27,-35,43,-15,36,42,-1,-29,12,-23,40,9,13,-24,-10,-24,22,-14,-39,18,17,-21,32,-20,12,-27,17,-15,-21,-48,-28,8,19,17,43,6,-39,-8,-21,23,-29,-31,34,-13,48,-26,-35,20,-37,-24,41,30,6,23,12,20,46,31,-45,-25,34,-23,-14,-45,-4,-21,-37,7,-26,45,32,-5,-36,17,-16,14,-7,0,37,-42,26,28]
    B = [38,34,-47,1,4,49,-18,10,26,18,-11,-38,-24,36,44,-11,45,20,-16,28,17,-49,47,-48,-33,42,2,6,-49,30,36,-9,15,39,-6,-31,-10,-21,-19,-33,47,21,31,25,-41,-23,17,6,47,3,36,15,-44,33,-31,-26,-22,21,-18,-21,-47,-31,20,18,-42,-35,-10,-1,46,-27,-32,-5,-4,1,-29,5,29,38,14,-22,-9,0,43]

    obj = Solution()
    b = obj.solve(A,B)
    print(len(b), b)


    a = [97,
    95,
    95,
    95,
    95,
    94,
    94,
    93,
    93,
    93,
    93,
    92,
    92,
    92,
    92,
    92,
    92,
    92,
    91,
    91,
    91,
    91,
    90,
    90,
    90,
    90,
    90,
    90,
    90,
    90,
    90,
    90,
    89,
    89,
    89,
    89,
    89,
    89,
    89,
    89,
    88,
    88,
    88,
    88,
    88,
    88,
    88,
    88,
    87,
    87,
    87,
    87,
    87,
    87,
    87,
    87,
    87,
    86,
    86,
    86,
    86,
    86,
    86,
    86,
    86,
    85,
    85,
    85,
    85,
    85,
    85,
    85,
    85,
    84,
    84,
    84,
    84,
    84,
    84,
    84,
    84,
    84,
    84]
    ls = []
    for i in range(len(a)):
        ls.append([a[i], b[i]])
    print(ls)


