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