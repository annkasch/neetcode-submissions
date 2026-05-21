class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        t = 0
        while t < len(tokens):

            try:
                stack.append(int(tokens[t]))
            except ValueError:
                a = stack.pop()
                b = stack.pop()
                if tokens[t] == "+":
                    stack.append(b + a)
                elif tokens[t] == "-":
                    stack.append(b - a)
                elif tokens[t] == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))

            t += 1
        
        return stack[0]

        