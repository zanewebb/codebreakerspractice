# fourth time

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = [0]*26
        ans = collections.defaultdict(list)
        
        for s in strs:
            counts = [0]*26
            for c in s:
                counts[ord(c)-97] += 1
            sig = "".join([str(x) for x in counts])
            ans[sig].append(s)
            
        return ans.values()



# third time
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        
        for w in strs:
            wrdsig = [0] * 26
            for c in w:
                wrdsig[ord(c) - 97] += 1
            ans["".join([str(x) for x in wrdsig])].append(w)
        
        return ans.values()

# second time

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        
        for s in strs:
            wrdsig = [0] * 26
            for c in s:
                wrdsig[ord(c)-ord("a")] += 1
            
            ssig = ""
            for n in wrdsig:
                ssig += str(n)
            
            if ssig in wordDict:
                wordDict[ssig].append(s)
            else:
                wordDict[ssig] = [s]
        # print(wordDict)
        
        return wordDict.values()

# first try, meh solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # not space efficient but
        
        # create dict
        angs = {}
        # store word signature array
        wrdsig = [0]*26
        
        # iterate across each string
        for s in strs:
            # increment the int at the index for the char's value
            for c in s:
                wrdsig[ord(c) - ord("a")] += 1
                
            # convert the wrdsig to a string representing it 
            # example: "00100002000030100002" or something
            ssig = ""
            for n in wrdsig:
                ssig += str(n)
                
            # store that as the key to the dict
            # if there isnt an entry for it yet, add one [current string]
            if ssig not in angs:
                angs[ssig] = [s]
            
            else:
                angs[ssig].append(s)
                
            # reset wrdsig
            wrdsig = [0] * 26
        return angs.values()