# fifth time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, r, bestWindow = 0, 0, 0
        
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                bestWindow = max(bestWindow, len(window))
            else:
                while s[r] in window and l <= r:
                    window.discard(s[l])
                    l += 1
                window.add(s[r])
            
            r += 1
        
        return bestWindow
        

class Solution:

    # fourth time
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        l = 0
        for c in s:
            if c in seen:
                while len(seen) > 0 and c in seen:
                    seen.discard(s[l])
                    l += 1
            seen.add(c)
            best = max(best, len(seen))
        return best  

    # third time, makes sense, similar solution strat to sub arrays product less than k
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if not s:
            return 0
        
        # set
        charSet = set()
        
        # iterate with window, add to set, 
        l = r = bestLen = 0
        while r < len(s):
            # when the next char is in the set already, 
            
            while s[r] in charSet:
                # move the window closed removing chars until that's no longer the case
                charSet.discard(s[l])
                l += 1
                
            charSet.add(s[r])
            
            bestLen = max(bestLen, len(charSet))
            
            r += 1
        
        return bestLen

        

   #second try, marginally better

   def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if not s:
            return 0
        
        #space inefficient solution
        
        bestMax = 0
        winChars = set()
        l = r = 0
        
        while r < len(s):
            if s[r] not in winChars:
                winChars.add(s[r])
            else:
                while s[r] in winChars:
                    winChars.discard(s[l])
                    l += 1
                winChars.add(s[r])
            bestMax = max(bestMax, len(winChars))
            
            r += 1
        return bestMax

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