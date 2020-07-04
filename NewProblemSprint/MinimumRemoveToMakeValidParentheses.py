# rough but i got it
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        closerproblems = set()
        opencount = 0
        closecount = 0
        
        for i,c in enumerate(s):
            if c is "(":
                opencount += 1
            elif c is ")":
                closecount += 1
                if closecount > opencount:
                    closerproblems.add(i)
                    closecount -= 1
        
        # construct answer string
        ans = ""
        opencount = closecount
        print(opencount,closecount)
        for i, c in enumerate(s):
            if i in closerproblems:
                closerproblems.discard(i)
                continue
            elif c == "(" and opencount > 0:
                ans += "("
                opencount -= 1
            elif c not in "(":
                ans += c
        
        return ans
        
        
        


# close to having a solution, couldnt do it sadly ...

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
        
        