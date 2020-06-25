class Solution:
    # accepted solution
    def topKFrequent(self, words, k):
        # counter object counts occurences of each element in a list
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]

    # first try, stupid non working solution
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # slow solution but
        
        # create dict for each word
        # { word: count }
        wd = {}
        # iterate over list of strings
        for w in words:
            # if the key isnt in the dict
            if w not in wd:
                # add it and set the count to 1
                wd[w] = 1
            # if it is in the dict
            else:
                # increment its count
                wd[w] += 1
        # return the slice (of length k) of the sorted keys 
        wordCounts = sorted(list(zip(wd.keys(), wd.values())), key=lambda x: x[1])
        wd = {}
        for w,c in wordCounts:
            if c in wordCounts:
                wd[c].append(w)
            else:
                wd[c] = [w]
        
        wordCounts = sorted(list(zip(wd.keys(), wd.values())), key=lambda x: x[0])
        
        ans = []
        i = len(wordCounts)
        while k > 0:
            while k > 0:
                
            
        return wordCounts[-k]