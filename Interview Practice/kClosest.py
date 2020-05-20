# yay heaps learning helped

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = []

        # [x, y]
        for p in points:
            pq.append( (math.sqrt(p[0]**2 + p[1]**2), p) )

        # heapify the list --> heap
        heapq.heapify(pq)

        # create ans list
        ans = []

        # for i in range(k):
        for i in range(K):
            # heapq.heappop(pq) into ans list
            ans.append(heapq.heappop(pq)[1])

        # return ans list
        return ans