
# second time

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)
        #print(list(word_counts))
        sorted_words = sorted(list(word_counts), key=lambda x: (-word_counts[x], x))
        print(sorted_words)
        
        return sorted_words[:k]