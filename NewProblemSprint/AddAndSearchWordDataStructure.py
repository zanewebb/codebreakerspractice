# got it
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = collections.defaultdict(set)
        
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.values[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for w in self.values[len(word)]:
            for i, c in enumerate(w):
                if word[i] != c and word[i] != ".":
                    break
                elif i == len(word)-1:
                    return True
        
        return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# had to look at the third case for search again
# have to look at each character on each word in the set for that key :/
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # length of word : set of word permutations with .
        self.words = collections.defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        key = len(word)
        
        for i in range(key):
            self.words[key].add(word[:i] + "." + word[i+1:])        
        
        self.words[key].add(word)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.words:
            return False
        if "." not in word:
            return True if word in self.words[len(word)] else False
        else:
            for w in self.words[len(word)]:
                matches = True
                for i,c in enumerate(word):
                    if c != w[i] and c != ".":
                        matches = False
                        break
                if matches:
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# third time, had to look at solution, forgot implemntation of search
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = collections.defaultdict(set)
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.values[len(word)].add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        elif "." not in word:
            return True if word in self.values[len(word)] else False
        else:
            for w in self.values[len(word)]:
                matches = True
                for i,c in enumerate(word):
                    
                    if c != w[i] and c != ".":
                        # if this char isnt a wildcard and it doesnt match that same
                        # index of the word we have in our values that we're investigating
                        # skip this word
                        matches = False
                        break
                if matches:
                    return True
            return False
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



# second time, didnt remember the concise solution, slow to execute this solution again
class Node:
    def __init__(self):
        self.children = {}
        self.val = None
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.val = word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        print(word)
        return self.rsearch(word, self.root, len(word))
        
        
    def rsearch(self, word, node, wordlen):
        found = False
        for i, c in enumerate(word):
            # print(c)
            if c == ".":
                # print("kicking off recursive calls")
                for k in node.children.keys():
                    found = found or self.rsearch(word[i+1:], node.children[k], wordlen)
                return found
            elif c not in node.children:
                return False
            else:
                node = node.children[c]
        
        # print("exited loop at node with val", node.val)
        if node.val and len(node.val) == wordlen:
            return True
        
        return False
    

        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# found this solution in forums, much faster, concise
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(set)
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].add(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False


# got it first time, little messy but works. Wildcard handling was wack

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.val = word
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        #print("searching for", word)
        return self.rsearch(self.root, word, 0)
        
        
    def rsearch(self, cur, partword: str, count: int):
        #print("began another rsearch with partword: ",partword, "and word", word)
        for i in range(len(partword)):
            # need to track count to measure word length
            count += 1
            
            # kick off another layer of search for the wildcard
            if partword[i] == ".":
                found = False
                for k in cur.children.keys():
                    found = found or self.rsearch(cur.children[k], partword[i+1:], count)#, word)
                return found
            # if it is a normal letter and we have it
            elif partword[i].isalpha() and partword[i] in cur.children:
                cur = cur.children[partword[i]]
                
            # otherwise we've hit a dead end
            else:
                return False
        #print("cur ended at", cur.val, "and count", count)
        return True if cur.val and len(cur.val) == count else False
        
class Node:
    def __init__(self):
        self.children = {}
        self.val = None

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)