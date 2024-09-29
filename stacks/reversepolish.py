class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        operators = ["+","-","*","/"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == "+":
                    stack.append(num2+num1)
                elif token == "*":
                    stack.append(num2*num1)
                elif token =="/":
                    stack.append(num2/num1)
                else:
                    stack.append(num2-num1)
        return int(stack[0])
    
sol = Solution()
list = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol.evalRPN(list)