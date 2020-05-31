
# second time, way overthought it
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        for n in nums:
            heapq.heappush(largest, n)
            while len(largest) > k:
                heapq.heappop(largest)
        return heapq.heappop(largest)

# first time, after solving different way
import heapq

class Solution:


   
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        
        for n in nums[:k]:
            heapq.heappush(pq, n)
        
        for n in nums[k:]:
            if n > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, n)
        
        return pq[0]