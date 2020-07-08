# forgot that my 2 pass solution TLE's, need to try this one next time
class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)


# way simpler version
class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)   


# TLE on the final case, O(2N) submission isn acceptable apparently


class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(" ", "")
        exp = []
        num = ""
        for c in s:
            if c in "/*+-":
                exp.append(int(num))
                num = ""
                exp.append(c)
            else:
                num += c
        exp.append(int(num))
        # print(exp)
        
        # iterate across once, doing multiplication and division left to right
        newexp = []
        i = 0
        while i < len(exp):
            if exp[i] == "*":
                self.operate(exp, i)
            elif exp[i] == "/":
                self.operate(exp, i)
            else:
                i += 1
            
        # then do the same for + and -
        i = 0
        while i < len(exp):
            if exp[i] == "+":
                self.operate(exp, i)
            elif exp[i] == "-":
                self.operate(exp, i)
            else:
                i += 1
        # print(exp)
        return exp[0]
                
    def operate(self, exp, i,):
        num1 = int(exp.pop(i-1))
        num2 = int(exp.pop(i))
        operator = exp.pop(i-1)
        i -= 1
        if operator == "*":
            exp.insert(i, num1 * num2)
        elif operator == "/":
            exp.insert(i, num1 // num2)
        elif operator == "-":
            exp.insert(i, num1 - num2)
        elif operator == "+":
            exp.insert(i, num1 + num2)
        # [2, *, 3]
        # [*]
        
        # [1, +, 2, *, 3]
        # [*, 3]
        
        
        