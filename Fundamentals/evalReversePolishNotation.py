# fourth time


def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    
    for i in range(len(tokens)):
        if tokens[i] in "+-/*":
            # calculate sub expression
            num1 = stack.pop()
            num2 = stack.pop()
            if tokens[i] == "+":
                stack.append(num1+num2)
            if tokens[i] == "-":
                stack.append(num2-num1)
            if tokens[i] == "/":
                stack.append(int(num2/num1))
            if tokens[i] == "*":
                stack.append(num1*num2)
            
        else:
            stack.append(int(tokens[i]))
        
    return stack.pop()





# third time

 def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for s in tokens:
            if s in "-+/*":
                num1 = stack.pop()
                num2 = stack.pop()
                if s == "+":
                    stack.append(num1+num2)
                if s == "-":
                    stack.append(num2-num1)
                if s == "*":
                    stack.append(num1*num2)
                if s == "/":
                    stack.append(int(num2/num1))
            else:
                stack.append(int(s))
        
        return stack.pop()




# second time

def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(0, len(tokens)):
            operators = "+-*/"
            
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            
            if tokens[i] in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(num2+num1)
                if tokens[i] == "-":
                    stack.append(num1-num2)
                if tokens[i] == "*":
                    stack.append(num2*num1)
                if tokens[i] == "/":
                    stack.append(int(num1/num2))
        return stack.pop()






def evalRPN(self, tokens: List[str]) -> int:
        # given input if valid should always have an operator at the end of the array
        # at a minimum, a valid expression should have number, number, expression as its least
        # complete input
        #-----------------------------------------------------------------------------------------
        
        # Build a stack which will house numbers in the expression until hitting an operator
        stack = []
        
        # as you iterate across the array, push numbers in 
        # when you hit an operator, pop the most recent 2 numbers and use the operator to perform a calculation
        # then push that result into the stack again
        for i in range(0, len(tokens)):
            if tokens[i].isdigit() or (tokens[i][0:1] == "-" and len(tokens[i]) >= 2):
                stack.append(int(tokens[i]))
            if tokens[i] in ["+", "-", "*", "/"]:
                stack = operate(stack, tokens[i])
        
        # when the array is complete there should be one single value in the stack, pop that and return it
        return stack.pop()
        
        
def operate(stack: List[int], operator: str):
    num1 = stack.pop()
    num2 = stack.pop()
    if operator == "+":
        stack.append(num2+num1)
        return stack
    if operator == "-":
        stack.append(num2-num1)
        return stack
    if operator == "*":
        stack.append(num2*num1)
        return stack
    if operator == "/":
        stack.append(int(num2/num1))
        return stack