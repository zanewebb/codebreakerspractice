
# first try, for some reason got it in my head that a set would work for anagrams pff

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # sliding window?
        l, r = 0, 0
        
        # using list
        need = [0] * 26
        for c in p:
            need[ord(c)-97] += 1
        
        have = [0] * 26
        ans = []
        
        
        while r < len(s):
            # extend window until required letters have been collected
            have[ord(s[r]) - 97] += 1
            
            if sum(have) >= sum(need):
                # close window until len of window equals length of p
                # print("START l, r : ",l,r)
                while r - l + 1 > len(p):
                    have[ord(s[l]) - 97] -= 1
                    l += 1
                # print("END l, r : ",l,r)
                    
                # if the set still contains the required letters, record l, else do nothing
                if have == need:
                    ans.append(l)
            r += 1
        
        return ans