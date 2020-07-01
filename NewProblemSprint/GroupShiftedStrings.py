
# had to look it up
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifts = collections.defaultdict(list)
        # print(shifts)
        
        for s in strings:
            key = ()
            for i in range(len(s)-1):                
                shift = 26 + ord(s[i+1]) - ord(s[i])
                key += (shift % 26,)
                
            shifts[key].append(s)
                # shifts[key] = shifts.get(key, []) + [s]
                
        return shifts.values()
        
        
        

# was close in my conceptual answer but wouldnt have figured out ---

def groupStrings(self, strings: List[str]) -> List[List[str]]:
	hashmap = {}
	for s in strings:
		key = ()
		for i in range(len(s) - 1):
         # --- this line. Had something similar but not correct
			circular_difference = 26 + ord(s[i+1]) - ord(s[i])
			key += (circular_difference % 26,)
		hashmap[key] = hashmap.get(key, []) + [s]
	return list(hashmap.values())