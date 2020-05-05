class Solution(object):

   # implemented the accepted solution after looking at it
   def partitionLabels(self, S: str) -> List[int]:
        # create and populate a dict which stores the last index of each char
        # this is critical because it tells us the bounds for what any given partition could be 
        # based on the chars within it
        last_indicies = {}
        for i,c in enumerate(S):
            last_indicies[c] = i
        
        l = r = 0
        ans = []
        for i, c in enumerate(S):
            # move the right edge of the current partition outwards to the required farthest right index for the char
            # in this substring
            r = max(r , last_indicies[c])
            
            # if the iterator index is equal to our farthest index for the chars in this substring, we have a partition
            if i == r:
                ans.append(len(S[l:r])+1)
                # reset the left side of the index to be the next index
                l = i + 1
        
        return ans


   # accepted solution

    def partitionLabels(self, S):
       # dictionary with each character and its rightmost index
        last = {c: i for i, c in enumerate(S)}
        
        # track pointers for left end of partition and right end of partition
        j = anchor = 0
        ans = []

        # iterate over chars in string
        for i, c in enumerate(S):

            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans