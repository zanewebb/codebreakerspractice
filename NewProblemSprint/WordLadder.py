
# ouch, need to study this one
class Solution:
    def __init__(self):
        self.wordcombos = collections.defaultdict(list)
        self.endWord = None
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset or not beginWord or not endWord or not wordList:
            return 0
        
        self.endWord = endWord
        
        for w in wordList:
            # go through each char in each word and replace it with a wildcard
            for i in range(len(w)):
                self.wordcombos[w[:i] + "." + w[i+1:]].append(w)
        
        print(self.wordcombos)
        
        
        queue = deque([(beginWord, 1)])
        # seen could also be a set
        seen = {beginWord:1}
        ans = 0
        
        while queue:
            word, steps = queue.popleft()

            # using the word at hand, try all permuations of this word with wildcards
            for i in range(len(word)):
                testword = word[:i] + "." + word[i+1:]
                
                # for each permutation, get its list of associated words
                for w in self.wordcombos[testword]:
                    # if we found our target then we return the ans (BFS means this should be the shortest path i think)
                    if w == self.endWord:
                        return steps + 1
                    
                    # if this word is not the answer, then we add it to our queue of steps to take, because this word
                    # might be part of the path to our answer word
                    if w not in seen:
                        seen[w] = steps + 1
                        queue.append((w, steps + 1))

                # wipe out this permutation list after checking each word in here, they are already part of
                # our queue and going to be considered, we don't want to revisit or waste time
                # checking if we've visited those words
                self.wordcombos[word] = []
                    
        return ans
        
        
        
        
        


# I had kinda the right idea, went about it wrong   

from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

# couldnt get it    
class Solution:
    def __init__(self):
        self.graph = None
        self.beginWord = None
        self.endWord = None
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0
        
        self.beginWord = beginWord
        self.endWord = endWord
        
        # collect the letter counts for each word
        wordcounts = {}
        wordList.append(beginWord)
        for w in wordList:
            lettercounts = collections.Counter(w) 
            wordcounts[w] = lettercounts
            
        # create a graph of words that are only one letter off from each other
        graph = collections.defaultdict(set)
        for w1 in wordList:
            for w2 in wordList:
                netcounts = wordcounts[w1] - wordcounts[w2]
                if abs(sum(netcounts.values())) == 1:
                    graph[w1].add(w2)
                    graph[w2].add(w1)
        
        print(graph)
        self.graph = graph
        fewest = self.DFS(beginWord, 1, set())
        return fewest if fewest < 99999 else 0
        
    def DFS(self, word, tfcount, seen):
        # print("checking word", word, "tfcount", tfcount)
        if self.endWord in self.graph[word]:
            return tfcount + 1

        fewest = 99999
        seen.add(word)
        for w in self.graph[word]:
            if w not in seen:
                fewest = min(fewest, self.DFS(w, tfcount + 1, seen.copy()))

        return fewest
        
        