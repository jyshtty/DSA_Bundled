# Find the k closest elements to X
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        
        heap = []
        heapify(heap)
        
        for i in arr:
            diff = abs(x-i)
            heappush(heap, [diff, i])
        
        ans = []
        for i in range(k):
            diff, n = heappop(heap)
            ans.append(n)
        
        return sorted(ans)
