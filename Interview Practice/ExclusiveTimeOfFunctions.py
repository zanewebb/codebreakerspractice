# Found this solution, pretty similar except you keep track of the "current time"
# and each time you read a log you add the time between the last log and the current log
# to the function on the top of the call stack
class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        total = [0 for i in range(n)]
        s = []
        i = 0
        curTime = 0
        while( i < len(logs)):
            curLog = logs[i].split(":")
            curId = int(curLog[0])
            status = curLog[1]
            nextTime = int(curLog[2])
            if (status ==  "start"):
                if (s):
                    total[s[-1]]+= nextTime - curTime
                s.append(curId)
                curTime = nextTime
            else:
                total[s[-1]]+= nextTime - curTime + 1
                s.pop()
                curTime = nextTime + 1
            i+=1
        return total


# i feel like this one should work, passes first 10 cases but fails with wrong answer

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # function list based on n for size
        funcs = [0] * n
        # stack for our order of functions called 
        stack = []
        
        # iterate over logs
        for log in logs:
            print("parsing log", log)
            parsedlog = log.split(":")
            parsedlog[0] = int(parsedlog[0])
            parsedlog[2] = int(parsedlog[2])
            # when we encounter a start log
            if parsedlog[1] == "start":
                # push that function ID onto the call stack
                stack.append(parsedlog[0])
                
                # subtract the time val from that func in the funcs list
                funcs[parsedlog[0]] -= parsedlog[2]
                # print("after starting log", funcs)
            # if we encounter an end log,
            elif parsedlog[1] == "end":
                
                # add the time val to the right function in the funcs list
                funcs[parsedlog[0]] += parsedlog[2] + 1
                
                # pop one val from the stack
                stack.pop()
                
                # subtract the val we just updated from the function on the top of the stack
                # (if there is one left on the stack)
                if len(stack) > 0:
                    funcs[stack[-1]] -= funcs[parsedlog[0]]
                # print("after ending log", funcs)
        return funcs
    
    
    
    '''
    [0,0]
    
    0:s:0 --> [0,0]
    1:s:2 --> [0,-2]
    1:s:5 --> [-4,4]
    1:s:6 --> [3,4]
    '''
            
        
        
        