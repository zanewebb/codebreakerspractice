
 def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        opensides = [];
        
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