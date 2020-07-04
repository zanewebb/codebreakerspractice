# worse than my first time, works though 
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = deque()
        
        while A and B:
            # pop while a's end is less than b's start
            while A and B and A[-1][1] < B[-1][0]:
                B.pop()
            
            # pop while a's end is less than b's start
            while A and B and B[-1][1] < A[-1][0]:
                A.pop()
                
            if A and B and A[-1][1] >= B[-1][0]:
                print(A[-1], B[-1])
                ans.appendleft([max(A[-1][0], B[-1][0]), min(A[-1][1], B[-1][1])])
                
                if A[-1][0] < B[-1][0]:
                    B.pop()
                else:
                    A.pop()
            
        return ans


# first try wow, good speed and eff too

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        A = deque(A)
        B = deque(B)
        ans = []
        
        while len(A) > 0 and len(B) > 0:
            start = -1
            end = -1
            
            if A[0][1] < B[0][0]:
                A.popleft()
            elif B[0][1] < A[0][0]:
                B.popleft()
            else:
                start = max(A[0][0], B[0][0])
                end = min(A[0][1], B[0][1])
                ans.append([start,end])
                
                if A[0][1] > B[0][1]:
                    B.popleft()
                elif B[0][1] > A[0][1]:
                    A.popleft()
                else:
                    A.popleft()
                    B.popleft()
        
        return ans