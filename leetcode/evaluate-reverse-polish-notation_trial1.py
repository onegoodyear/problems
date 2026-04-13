class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a, b = None, None
        for token in tokens:
            if token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
        return stack[0]
