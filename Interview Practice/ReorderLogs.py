# third time 
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key = self.logSort)
    
    
    def logSort(self, log):
        splitLog = log.split(" ")
        if splitLog[1].isdigit():
            return (1,)
        else:
            return (-1, splitLog[1:], splitLog[0])


# second time ?
class Solution:
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    return sorted(logs, key=self.sorter)
def sorter(self, a):
    if a.split(" ")[1].isdigit():
        return (1,)
    else:
        return (-1,a.split(" ")[1:],a.split(" ")[0])

class Solution:

   # got it first time! 
   # probably could be more optimal if you held onto the identifiers as the keys to whether or not theyre letter or digit logs but

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for l in logs:
            # if the first word (non identifier) in the log's first character is a number
            # then add it to the digit logs
            if l.split(" ")[1][0] in "1234567890":
                digit_logs.append(l)
            else:
                letter_logs.append(l)
                
        return sorted(letter_logs, key=lambda x: (x.split(" ")[1:], x.split(" ")[0])) + digit_logs 