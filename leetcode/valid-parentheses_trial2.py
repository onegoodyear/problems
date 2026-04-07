class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        for ch in s:
            if ch in {'[', '{', '('}:
                stack.append(ch)
            else:
                if stack:
                    br = stack.pop()
                    if ch != pairs[br]: return False
                else: return False
        else:
            return False if stack else True
        