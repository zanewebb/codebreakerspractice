# maxProfitAssignment

class Solution:

   # Provided solution #1 
   def maxProfitAssignment(self, difficulty, profit, worker):
      jobs = zip(difficulty, profit)
      jobs.sort()
      ans = i = best = 0
      for skill in sorted(worker):
         while i < len(jobs) and skill >= jobs[i][0]:
               best = max(best, jobs[i][1])
               i += 1
         ans += best
      return ans


   # another throwaway solution, cant figure out how to choose the "next highest from worker's difficulty if their difficulty is not present"
   def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # for each worker we want to consider jobs within their difficulty ceiling
        # then we want that worker to complete whatever is the max() of the profitability associated with
        # the tasks what are able to be completed by that worker
        
        # Dict which has keys of the difficulties, and a max profit for each stored difficulty level
        profitDict = {}
        
        # assuming these are sorted, which I'm not sure I can do
        for i in range(len(difficulty)):
            profitDict[difficulty[i]] = max(profit[0:i])
        
        totalProfit = 0
        #iterate over workers adding the profits of their difficulty
        for emp in worker:
            
        
        
        
        return totalProfit

   # throwaway solution, sorting the lists wrecks their association
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # for each worker we want to consider jobs within their difficulty ceiling
        # then we want that worker to complete whatever is the max() of the profitability associated with
        # the tasks what are able to be completed by that worker
        
        # UNSURE IF THESE WILL ALWAYS BE SORTED???
        
        difficulty = sorted(difficulty)
        profit = sorted(profit)
        worker = sorted(worker)
        
        totalProfit = 0
        
        # edge case where no worker can accomplish any task
        if worker[-1] < difficulty[0]:
            return 0
        
        # iterate down the workers 
        for emp in worker:
            # move a pointer down the difficulty list until the pointer is either at their difficulty limit or 
            # at least the highest within their capabilities
            diffInd = 0
            while difficulty[diffInd] <= emp and diffInd < len(difficulty)-1:
                diffInd += 1
            
            if difficulty[diffInd] > emp:
                diffInd -= 1
                
            # using that index, find the associated max() within profit[] and add that value to the total profit
            totalProfit += max(profit[0:diffInd])
        
        return totalProfit