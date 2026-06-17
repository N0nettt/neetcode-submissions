class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = { ")" : "(", "}": "{", "]":"["}


        print(f"stack: {stack}")
        for c in s:
            if c in d:
                if stack and d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return len(stack) == 0
            