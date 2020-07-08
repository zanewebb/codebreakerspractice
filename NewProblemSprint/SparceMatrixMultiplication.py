# much cleaner
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for arow in range(len(A)):
            ansrow = []
            for bcol in range(len(B[0])):
                acol = 0
                brow = 0

                tempsum = 0
                # A col and B row are equivalent so only need one condition
                while acol < len(A[0]):
                    tempsum += A[arow][acol] * B[brow][bcol] 
                    acol += 1
                    brow += 1
                
                ansrow.append(tempsum)
            ans.append(ansrow)
        return ans
                


# second time, need to use whiles
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for Arow in A:
            currow = []
            Bcolind = 0
            while Bcolind < len(B[0]):
                add = 0
                Acolind = 0
                while Acolind < len(A[0]):
                    for Brow in B:
                        # print("multiplying ", Arow[Acolind], Brow[Bcolind])
                        add += Arow[Acolind] * Brow[Bcolind]
                        Acolind += 1
                currow.append(add)
                Bcolind += 1
            ans.append(currow)
        
        return ans
            



# kljnkjnawdknawdjn
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        if eleB: C[i][j] += eleA * eleB
        return C