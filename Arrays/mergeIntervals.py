#mergeIntervals.py


class Solution:

   #same solution with a sort at the beginning
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        # iterate over the intervals
        i = 1
        # print(len(intervals))
        while i < len(intervals) and len(intervals) > 1:
            # for each one, if the start of the interval is less than the end of the one before it
            # and the end of the curent interval is bigger than the beginning of the previous
            if intervals[i][0] <= intervals[i-1][1] and intervals[i][1] >= intervals[i-1][0]:
                # update the end of the previous interval to equal the bigger end
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                # update the beginning of the previous interval to equal the smaller beginning
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
                # pop the current interval
                intervals.pop(i)
            
            # else, increment i
            else:
                i += 1
         return intervals


         

   #first try, dumb solution that hinges on it being sorted already
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        # iterate over the intervals
        i = 1
        # print(len(intervals))
        while i < len(intervals) and len(intervals) > 1:
            # for each one, if the start of the interval is less than the end of the one before it
            # and the end of the curent interval is bigger than the beginning of the previous
            if intervals[i][0] <= intervals[i-1][1] and intervals[i][1] >= intervals[i-1][0]:
                # update the end of the previous interval to equal the bigger end
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                # update the beginning of the previous interval to equal the smaller beginning
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
                # pop the current interval
                intervals.pop(i)
            
            # else, increment i
            else:
                i += 1
        
        if len(intervals) < 2:
            return intervals
        
        # traverse the other direction
        i = len(intervals)-2
        while i >= 0 and len(intervals) > 1:
            #print(i, intervals)
            # for each one, if the start of the interval is less than the end of the one before it
            # and the end of the curent interval is bigger than the beginning of the previous
            if intervals[i][0] <= intervals[i+1][1] and intervals[i][1] >= intervals[i+1][0]:
                # update the end of the previous interval to equal the bigger end
                intervals[i+1][1] = max(intervals[i+1][1], intervals[i][1])
                # update the beginning of the previous interval to equal the smaller beginning
                intervals[i+1][0] = min(intervals[i+1][0], intervals[i][0])
                # pop the current interval
                intervals.pop(i)
                i -= 1
            # else, decrement i
            else:
                i -= 1
        
        return intervals