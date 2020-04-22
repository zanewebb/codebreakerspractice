# canCompleteCircuit.py

class Solution:

    #fourth time
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        if len(gas) == 1:
            return 0
        
        # zip the gas and costs together to form stations
        stations = list(zip(gas, cost))
        # track curGas and bestStation
        curGas, bestStation = 0, None
        # iterate over stations
        for i,station in enumerate(stations):
            # add the station's net gas to the curGas
            curGas += station[0] - station[1]
            # if the curGas is less than 0, reset bestStation to none and reset curGas
            if curGas < 0:
                curGas = 0
                bestStation = None
            # if curGas is above zero and bestStation is none, set best station to the current station
            if curGas > 0 and bestStation is None:
                bestStation = i
            # print("curGas ", curGas)
            # print("bestStation ", bestStation)
        return bestStation

    #third time, almost clean execution, stumbled on (second) station setting condition

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        # if the total gas available is less than the total cost required, cant make it
        if sum(gas) < sum(cost):
            return -1
        
        # funny edge case from leetcode that i love thank you very much hehe funny
        if len(gas) == 1:
            return 0
        
        # track the station in question, and the current gas
        station, curGas = -1, 0
        
        # zip the gas and costs of the station together, do not sort it
        stations = list(zip(gas,cost))
        
        # iterate over the stations
        for i,s in enumerate(stations):
            # add the net gas of the current station
            curGas += s[0] - s[1]
            #print("curGas is: ", curGas)
            
            # if our current gas is less than 0
            if curGas < 0:
                # reset the station tracker
                station = -1
                # reset the current gas
                curGas = 0
            
            # if the station tracker hasn't been set, set it to this station
            if station == -1 and curGas > 0:
                station = i
            #print("station is: ", station)
                
        return station


        

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