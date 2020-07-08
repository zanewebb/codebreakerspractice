# got it this time
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            longest = max(self.search(i, i, s), self.search(i, i+1, s), longest, key=len)
            
        return longest
    
    def search(self, l, r, s):
        ret = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ret = s[l:r+1]
            l -= 1
            r += 1
        return ret
            

# had trouble fully remembering the implementation but ihad it pretty close
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            ret = max(self.check(s,i,i), self.check(s,i,i+1), ret, key=len )
        
        return ret
            
    def check(self, s, start, end):
        ret = ""
        while start >= 0 and end < len(s) and s[start] == s[end]:
            ret = s[start:end+1] 
            start -= 1
            end += 1
        return ret


# elegant solution

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

        return res
       
        
    def helper(self,s,l,r):
        
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]
            