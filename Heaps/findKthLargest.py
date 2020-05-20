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