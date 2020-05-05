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