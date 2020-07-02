# finally got it without looking 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskcounts = [0] * 26
        
        for t in tasks:
            taskcounts[ord(t) - 65] += 1
            
        maxcount = max(taskcounts)
        taskcounts = sorted(taskcounts)
        # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3]
        taskcounts.pop()
        
        idletime = (maxcount-1) * n
        print(idletime)
        # [A, -, -, A, -, -, A]
        
        # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
        for t in taskcounts :
            idletime -= min(maxcount-1, t)
            # print(idletime)
        
        idletime = max(idletime, 0)
        print(len(tasks) + idletime)
        return len(tasks) + idletime
        
        
        # [A, -, -, A, -, -, A]
        # [     ]
        



# forgot part of it, had to look at the ans
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskcounts = [0] * 26
        for t in tasks:
            taskcounts[ord(t) - 65] += 1
        
        taskcounts = sorted(taskcounts)
        
        maxfreq = taskcounts.pop()
        
        idletime = (maxfreq - 1) * n
        
        while idletime > 0 and taskcounts :
            # we subtract 1 from the max and perform this min
            # so that we cover an edge case where there are ties for the max freq
            # By doing this we arent over-reducing the idle time. If there is a tie
            # for the max freq then we dont get to freely sprinkle the task among the available open space
            # We instead have to account for 1 extra slot in the task order
            # In this example we can see that we initially place the necessary max space between our max freq task
            # input [A,A,A,B,B,B] n = 2
            # [A,-,-,A,-,-,A]
            #
            # but after discovering the tie for max freq, we have to extend the original estimate of task order length
            # by one because it doesnt fit within the allotted idle times
            # [A,B,-,A,B,-,A,B]
            
            idletime -= min(maxfreq-1, taskcounts.pop())
        
        idletime = max(0, idletime)
        
        return idletime + len(tasks)
            
        # [A,B,-,A,B,-,A,B]
        # [3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #  4 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        


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