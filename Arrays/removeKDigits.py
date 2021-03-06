# eight time???
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while len(stack) > 0 and int(n) < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(int(n))
        
        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1
        
        print(stack)
        
        ans = ""
        foundDigit = False
        while len(stack) > 0:
            popped = str(stack.pop(0))
            if popped in "123456789" or foundDigit:
                ans += popped 
                foundDigit = True
        
        if not ans:
            return "0"
        
        return ans


# seventh time

def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for n in num:
            while k > 0 and len(stack) > 0 and int(n) < stack[-1]:
                stack.pop()
                k -= 1
                
            stack.append(int(n))
            
        
        while k > 0 and len(stack) > 0:
            stack.pop()
            k -= 1
        
        ans = ""
        foundnonzero = False
        
        while len(stack) > 0:
            popped = str(stack.pop(0))
            
            if popped in "123456789" or foundnonzero:
                foundnonzero = True
                ans += popped
        
        if not ans:
            return "0"
        
        return ans

# sixtht ime
def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        
        stack = []
        
        for s in num:
            while len(stack) > 0 and k > 0 and int(s) < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(int(s))
        
        while len(stack) > 0 and k > 0:
            k -= 1
            stack.pop()
        
        
        #build answer
        seenNonZero = False
        ans = ""
        while len(stack) > 0:
            popped = stack.pop(0)
            if popped != 0 or seenNonZero:
                seenNonZero = True
                ans += str(popped)
        
        if len(ans) == 0:
            return "0"
        
        return ans

# fifth time
def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        
        stack = []
        
        for s in num:
            while len(stack) > 0 and int(s) < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(int(s))
        
        # edge case for all duplicate nums
        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1
        
        # build the answer string
        ans = ""
        leadingZero = True
        while len(stack) > 0:
            popped = stack.pop(0)
            
            if popped != 0 or not leadingZero:
                ans += str(popped)
                leadingZero = False
        
        if not ans:
            return "0"
        else:
            return ans 
 
# fourth time

def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        stack = []
        
        for i in range(len(num)):
            while len(stack) > 0 and k > 0 and stack[-1] > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(int(num[i]))
        
        while k > 0 and len(stack) > 0:
            stack.pop()
            k -= 1
        
        # build answer
        ans = ""
        leadingZero = True
        while len(stack) > 0:
            popped = stack.pop(0)                
            if (not leadingZero and popped == 0 ) or popped != 0:
                leadingZero = False
                ans += str(popped)
            
        if not ans:
            return "0"
        else: 
            return ans


 # third time

 def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        
        stack = []
        
        for i in range(len(num)):
            # for each number, check that it is the smallest number that we can put first in our final number
            while len(stack) > 0 and int(num[i]) < stack[-1] and k > 0:
                # for each number that we discard during this check, decrement k
                stack.pop()
                k -= 1
                
            stack.append(int(num[i]))
        
        # if there are still numbers to remove, just remove them from the stack until k is 0
        while k and len(stack) > 0:
            stack.pop()
            k -= 1
        
        # build the answer with leading zeros in mind
        ans = ""
        foundNum = False
        while len(stack) > 0:
            nextNum = stack.pop(0)
            if nextNum != 0:
                foundNum = True
            if (foundNum and nextNum == 0) or nextNum != 0:
                ans = ans + str(nextNum)
        
        # if the answer has no numbers, return a 0
        if not ans:
            return "0"
        
        return ans
 
 
 
 
 
 # second time

 def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        
        finalNumStack = []
        
        for i in num:
                while len(finalNumStack) > 0 and finalNumStack[len(finalNumStack)-1] > int(i) and k > 0:
                    finalNumStack.pop()
                    k -= 1
                    
                finalNumStack.append(int(i))
        
        # Edge case check
        while k > 0:
            k -= 1
            finalNumStack.pop()
        
        
        ans = ""
        foundNonZero = False
        print(finalNumStack)
        while len(finalNumStack) > 0:
            ansNum = finalNumStack.pop(0)
            if ansNum != 0:
                foundNonZero = True
            
            if (foundNonZero and ansNum == 0) or ansNum != 0:
                ans = ans + str(ansNum) 
        
        if not ans:
            return "0"
        return ans
 
 
 # first time
 
 def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == 0:
            return "0"
        
        stack = []
        
        # iterate over the nums in the list, 
        for i in range(len(num)):
            # add the number to a stack if it is less than the most recently added number  
            if len(stack) > 0 and stack[len(stack)-1] > int(num[i]) and k != 0: 
                if stack.pop() != -1:
                # each time one is substituted via deciding that a number is smaller than stack.peek, decrement k
                    k -= 1
            stack.append(int(num[i]))
        
        if k == 1:
            stack.pop()
        
        
        # when k == 0, pop from the stack adding to the front of the remainder of the num string (ommiting if 0)
        ans = ""
        leadingZeros = True
        while len(stack) > 0:
            popped = str(stack.pop(0))
            # print("Popped ",popped)
            # print("Ans:  ",ans)
            # print("leadingZeros ",leadingZeros)
            if (popped == "0" and not leadingZeros) or popped in "123456789":
                ans =  ans + popped
            if len(ans) > 0 :
                leadingZeros = False
        
        return ans if len(ans) > 0 else "0"