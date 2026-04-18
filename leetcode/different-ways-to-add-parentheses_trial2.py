class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i, ch in enumerate(expression):
            if ch in "*+-":
                left_outcome = self.diffWaysToCompute(expression[:i])
                right_outcome = self.diffWaysToCompute(expression[i+1:])
                for x in left_outcome:
                    for y in right_outcome:
                        if ch == "+":
                            res.append(x+y)
                        elif ch == "-":
                            res.append(x-y)
                        else: res.append(x * y)
        if not res: res.append(int(expression))
        return res
        

        