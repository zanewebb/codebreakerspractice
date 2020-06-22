# holy moly this one is hard, struggling to remember or construct the solution still

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        tCounter = collections.Counter(t)
        
        sInds = []
        for i,c in enumerate(s):
            if c in tCounter:
                sInds.append((i,c))
        
        # something like this
        # [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
        
        # how many characters are required in the best possible window
        requiredNumChars = len(tCounter)
        
        # we hold our answer as a 3 val tuple where the first spot is the distance, 
        # the second two are the indexes of the ends of the valid window
        minWindowLen = (99999999, None, None)
        
        windowCounts = {}
        currentNumChars = 0
        # iterate over our viable indicies 
        while r < len(sInds):
            # increment the count of this char in our hypothetical window
            windowCounts[sInds[r][1]] = windowCounts.get(sInds[r][1], 0) + 1
            
            # if the counts match for this specific char, incremenet the count of valid chars
            if windowCounts[sInds[r][1]] == tCounter[sInds[r][1]]:
                currentNumChars += 1
            
            # while it is still valid, close the window
            while l <= r and currentNumChars == requiredNumChars:
                
                # update the smallest window
                if sInds[r][0] - sInds[l][0] + 1 < minWindowLen[0]:
                    minWindowLen = (sInds[r][0] - sInds[l][0] + 1, sInds[l][0], sInds[r][0])
                
                # remove the count for the char at l
                windowCounts[sInds[l][1]] -= 1
                
                # if we no longer have a valid number of occurences for this char in our window
                # decrement our current valid char count
                if windowCounts[sInds[l][1]] < tCounter[sInds[l][1]]:
                    currentNumChars -= 1
                l += 1
                
            # stretch the window
            r += 1
        return "" if minWindowLen[0] == 99999999 else s[minWindowLen[1]:minWindowLen[2]+1]