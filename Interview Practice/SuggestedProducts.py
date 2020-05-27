
# fourth time

class Trie:
    def __init__(self):
        self.suggestions = []
        self.children = {}

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # create the suggestion tree
        root = Trie()
        cur = root
        
        for p in sorted(products):
            cur = root
            for c in p:
                # if the trie node isnt already there, make it
                if c not in cur.children:
                    cur.children[c] = Trie()
                
                # traverse the tree    
                cur = cur.children[c]
                
                # add the suggestions
                if len(cur.suggestions) < 3:
                    cur.suggestions.append(p)
                
        
        # mimick the keystrokes
        ans = []
        cur = root
        for ks in searchWord:
            if cur and ks in cur.children:
                cur = cur.children[ks]
                ans.append(cur.suggestions)
            else:
                cur = None
                ans.append([])
        
        return ans


# third time
class Trie:
    def __init__(self):
        self.suggestions = [] # list of words
        self.children = {} # dict of other tries

class Solution:
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # populate the search trie
        root = Trie()
        for p in sorted(products):
            cur = root
            for c in p:
                # the child trie exists, traverse to it
                if c in cur.children:
                    
                    cur = cur.children[c]
                    
                # the child trie does not exist, create it and add this word to its suggestions
                else:
                    cur.children[c] = Trie()
                    cur = cur.children[c]
                
                # adding this word to its suggestions
                if len(cur.suggestions) < 3:
                        cur.suggestions.append(p)
        
        # build the answer list of "keystrokes"
        ans = []
        cur = root
        for c in searchWord:
            if cur and c in cur.children:
                cur = cur.children[c]
                ans.append(cur.suggestions)
            else:
                cur = None
                ans.append([])
        
        return ans


# second attempt trie solution
class Trie:
    def __init__(self):
        # children point to the sub-trie's that have their respective suggestions for that search term
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # create the root, it stays empty
        root = Trie()
        
        # populate the trie
        for product in sorted(products):
            sub_trie = root
            
            for c in product:
                # create the node if it isnt there already
                if c not in sub_trie.children:
                    sub_trie.children[c] = Trie()
                
                # traverse downwards
                sub_trie = sub_trie.children[c] 
                
                # if space is available for this subterm, add this word as a suggested word
                if len(sub_trie.suggestions) < 3:
                    sub_trie.suggestions.append(product)
                    
        # run the "keystrokes"
        cur = root
        ans = []
        # for each char input, traverse one step to the proper node
        for c in searchWord:
            if cur and c in cur.children:
                cur = cur.children[c]
                ans.append(cur.suggestions)
            else:
                cur = None
                ans.append([])
        
        return ans
                


# found this solution 
def suggestedProducts(self, A, word):
        A.sort()
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, i)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return res

# and this one which is my solution but way better

# each trie node has a suggestion list and a children dict
class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestion = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
       # create the root tree
        root = Trie()

        # populate the tree with the products
        for product in sorted(products):
           # create a cur (iterator) to traverse the tree with
            trie = root

            # iterate over the letters in each product
            for char in product:
               # if the letter isnt in this node's children, create it
                if char not in trie.sub:
                    trie.sub[char] = Trie()
               # move to the next node
                trie = trie.sub[char]

               # if there's room for suggestions in this node, add it.
               # The reason for having this restriction is because we are
               # inputting the products ALPHABETICALLY so therefore,
               # the alphabetical, 3 suggestion limit is being met on the creation
               # of the tree rather than after gathering all results. 
                if len(trie.suggestion) < 3:
                    trie.suggestion.append(product)
      # begin "typing" the search word.
      # the way this one wors is that instead of traversing through the tree for each new "search term"
      # ex: "m" "mo" "mou" 
      # you instead have populated the tree in a way where each new letter holds all the answers
      # you are looking for, so as each letter is "typed" just move deeper into the tree
        ans = []
        for char in searchWord:
           # for each letter, using root as the iterator
           # move to the next node that is the next letter in the word
           # we return this node's suggestion set as the sub-searchterm's suggestions
           # because this question requires us to simulate 5 keystrokes, we add it to a list
            if root:
                root = root.sub.get(char, None)
            ans.append(root.suggestion if root else [])
        return ans



# first try, couldnt get the stupid search to get the right results, super close.
# started on root and wouldn't iterate to the "E" node on the word mouse so it didnt give the right answer set

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # create the b tree
        btree = BTree()
        # fill the b tree by inserting each word
        for product in products:
            btree.addWord(product)
            
        # search for the search term
        ans = []
        for i in range(0,len(searchWord)):
            print("Searching for", searchWord[:i+1])
            ans.append(btree.search(searchWord[:i+1]))
        
        return ans
        
class Node:
    def __init__(self, key):
        self.key = key
        self.vals = set()
        self.children = {} # key is the key (letter) and value is the node
        
class BTree:
    def __init__(self):
        self.root = Node("-1")
    
    def addWord(self, word):
        cur = self.root
        
        # for each letter of the word, check if the letter is in the children of the current node
        for c in word:
            # if not, create a node for that letter, append it to the children of this node
            if c not in cur.children:
                n = Node(c)
                n.vals.add(word)
                cur.vals.add(word)
                cur.children[c] = n
                
                # set the current node to be the node just entered
                cur = n
                
            else:
                # add the value to the node we're att
                cur.vals.add(word)
                
                # continue traversing
                cur = cur.children[c]   
    
    def search(self, searchTerm):
        # create a counter for returned items
        results = []
        cur = self.root
        
        
        # while the iterator for the letters isnt past the end
        # and the count isnt = or above 3
        i = 0
        while i < len(searchTerm):
            # append the values of this node's children that arent None
            newResults = [val for val in cur.vals]
            results = newResults 
            
            #move the current node
            if searchTerm[i] in cur.children:
                cur = cur.children[searchTerm[i]]
            else:
                break
            
            i += 1
            
        # sort the result set
        results.sort()
        
        # return the first 3
        return results[:3]
    
    # def printNodeVals(self, searchword):
        