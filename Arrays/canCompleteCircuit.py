# canCompleteCircuit.py

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        if sum(gas) < sum(cost):
            return -1
        
        if len(gas) == 1:
            return 0
        
        curGas = 0
        startStation = -1
        
        for i in range(len(gas)):
            curGas += gas[i] - cost[i]
            if startStation == -1 and curGas > 0:
                startStation = i
            
            if curGas < 0:
                startStation = -1
                curGas = 0
                
        return startStation