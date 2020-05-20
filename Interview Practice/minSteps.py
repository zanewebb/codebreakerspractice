
# first try baybeee
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # create Counter objects for both s and t
        sCounts = collections.Counter(s)
        tCounts = collections.Counter(t)

        #ccc abc
        # { b:2 a:1 }   { b:1 a:2 }
        # { c:3 }   { a:1 b:1 c:1 }

        # subtract one of those counter objects from the other
        sCounts.subtract(tCounts)

        # sum the total of the counts in the diff Counter
        keys = list(filter(lambda x: sCounts[x] >= 0, sCounts.keys()))
        count1 = 0
        for key in keys:
            count1 += sCounts[key]



        # return the lesser of the two
        return count1