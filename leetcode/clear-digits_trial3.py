class Solution:
    def clearDigits(self, s: str) -> str:
        def helper(i: int) -> str:
            if i >= len(s): return ""
            if i + 1 == len(s):
                return s[i]
            if s[i].isdigit():
                return s[i] + helper(i+1)
            if s[i+1].isdigit():
                return helper(i+2)
            next = helper(i+1)
            if next and next[0].isdigit():
                return next[1:]
            return s[i] + next
        
        return helper(0)
        