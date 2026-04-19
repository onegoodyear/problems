class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(i: int, j: int):
            if j == len(p):
                return i == len(s)
            
            matching = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j+1] == '*':
                if matching:
                    return helper(i, j+2) or helper(i+1, j)
                else:
                    return helper(i, j+2)

            if matching:
                return helper(i+1, j+1)
            
            return False

        

        return helper(0,0)