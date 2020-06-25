# accepted solution
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

         # we now have a list of all the frequencies of each task and they're sorted by freq

        # max frequency
        # we get the max freq and perform this calculation because it outlines what the max possible 
        # amount of idle slots there will have to be 
        '''
         ["A","A","A","B","B","B"], n = 2
         
         # order of execution
         [A, -, -, A, -, -, A]
         number of -'s = 4
         4 = ( (3 A's) - 1 ) x 2
         
         '''
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        # we chip away at our remaining idle time by "placing" the remaining tasks 
        # in the exec order
        # 
        '''
        # order of execution
         [A, B, -, A, B, -, A] B
        '''
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop()) # this min is to cover an edge case of ties with the max freq
        # we then make sure our idle is reset to 0 if it was negative, or we just hold onto the remaining time
        idle_time = max(0, idle_time)

         # make sure to add the remaining time 
        return idle_time + len(tasks)