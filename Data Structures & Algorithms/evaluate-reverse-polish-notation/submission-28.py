class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                res = stack.pop() + stack.pop()
                stack.append(res)
            
            elif t == '-':
                firstNumber, secondNumber = stack.pop(), stack.pop()
                stack.append(secondNumber - firstNumber)

            elif t == '*':
                res = stack.pop() * stack.pop()
                stack.append(res)                

            elif t == '/':
                firstNumber, secondNumber = int(stack.pop()), int(stack.pop())
                stack.append(int(secondNumber / firstNumber))
            
            else:
                stack.append(int(t))
            print(stack)

        return stack[-1]