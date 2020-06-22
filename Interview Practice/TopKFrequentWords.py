# fifth time

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCounts = collections.Counter(words)
        wordCounts = sorted(list(wordCounts.keys()), key=lambda x: (-wordCounts[x], x))
        return wordCounts[:k]
        

# fourth time, remembered it

def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)
        sorted_word_counts = sorted(list(word_counts), key= lambda x: (-word_counts[x], x))
        return sorted_word_counts[:k]


# third time

# i forgot the clean setup, still worked after some peeking
def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)
        sorted_word_counts = list(sorted(word_counts.items(), key=lambda wc: (-wc[1], wc[0])))
        sorted_word_counts = [wc[0] for wc in sorted_word_counts]
        return sorted_word_counts[:k]

# second time

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = collections.Counter(words)
        #print(list(word_counts))
        sorted_words = sorted(list(word_counts), key=lambda x: (-word_counts[x], x))
        print(sorted_words)
        
        return sorted_words[:k]