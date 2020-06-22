# second time, much cleaner I supposed
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key= lambda x: math.sqrt(x[0]**2 + x[1]**2) )[:K]


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