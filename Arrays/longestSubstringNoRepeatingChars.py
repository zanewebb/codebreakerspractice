class Solution:

   # first try, woohoo
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if not s:
            return 0
        
        # track max length and cur length and window start / end
        maxLength = curLength = end = st = 0
        windowChars = set()
        
        # iterate once over the string starting at 1
        while st < len(s):
            # if the char at the current s[st] isnt in the window set, add it and increment length
            if s[st] not in windowChars:
                curLength += 1
                windowChars.add(s[st])
                
                # if the current is better than the max, set the max to the current 
                if curLength > maxLength:
                    maxLength = curLength
            else:
                # while the char at s[st] is still in the window set, bring in the end pointer
                # removing each value from the window set
                while s[st] in windowChars:
                    windowChars.discard(s[end])
                    end += 1
                    curLength -= 1
                windowChars.add(s[st])
                curLength += 1
            st += 1
                
        # return max
        return maxLength