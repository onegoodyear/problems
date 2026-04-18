class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i: int):
            res = ""
            k = 0
            while i < len(s):
                if s[i].isdigit(): k = k * 10 + int(s[i])
                elif s[i] == "[":
                    inside, i = helper(i+1)
                    res += k * inside
                    k = 0
                elif s[i] == "]":
                    return res, i
                else: res += s[i]
                i += 1
            return res
        return helper(0)
        