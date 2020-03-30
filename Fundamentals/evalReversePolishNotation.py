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