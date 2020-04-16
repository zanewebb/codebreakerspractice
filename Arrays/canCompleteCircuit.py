# canCompleteCircuit.py

class Solution:

   # second time
   def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        # if the total gas available is less than the total cost required, cant make it
        if sum(gas) < sum(cost):
            return -1
        
        # HE HE FUNNY EDGE CASE thanks leetcode
        if len(gas) == 1:
            return 0
        
        # create list of paired station values
        netGas = list(zip(gas,cost))
        
        # track current gas, target station
        curGas = 0
        targetStation = -1
        
        for i in range(len(netGas)):
            # Add the net gas to the current gas each step
            curGas = curGas + netGas[i][0] - netGas[i][1]
            
            # If we run empty, reset the targetStation and current gas
            if curGas < 0:
                targetStation = -1
                curGas = 0
            if targetStation == -1 and curGas > 0:
                targetStation = i
                
        # return targetStation
        return targetStation






   # first time, couldnt do
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