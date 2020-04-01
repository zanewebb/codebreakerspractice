

# 3rd time
def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        
        for i in range(0, len(s)):
            if s[i] in ["{", "[", "("]:
                stack.append(s[i])
            if s[i] in ["}", "]", ")"]:
                if len(stack) == 0:
                    return False
                
                opener = stack.pop()
                if opener == "{" and s[i] != "}":
                    return False
                if opener == "[" and s[i] != "]":
                    return False
                if opener == "(" and s[i] != ")":
                    return False
        
        if len(stack) > 0:
            return False
        
        return True









 def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        opensides = []
        
        for i in range(0,len(s)):
            if s[i] in ["[", "{", "("]:
                opensides.insert(0, s[i])
            elif s[i] in ["]", "}", ")"]:
                if len(opensides) == 0:
                    return False
                opener = opensides.pop(0)
                if not compareBrace(opener, s[i]):
                    return False
                
        if len(opensides) > 0:
            return False
        return True        

            
def compareBrace(a:str, b:str):
    if a=="[" and b=="]":
        return True
    elif a=="{" and b=="}":
        return True
    elif a=="(" and b==")":
        return True
    else:
        return False



# second completion solution:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        opens = []
        
        for i in range(0,len(s)):
            if s[i] in ["{", "[", "("]:
                opens.insert(0, s[i])
            if s[i] in ["}", "]", ")"]:
                if len(opens) == 0:
                    return False
                
                opener = opens.pop(0)
                if opener == "{" and s[i] != "}":
                    return False
                if opener == "[" and s[i] != "]":
                    return False
                if opener == "(" and s[i] != ")":
                    return False
                
        if len(opens) > 0:
            return False
        
        return True