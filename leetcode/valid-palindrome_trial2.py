class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for ch in s:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
                t += ch.lower()
        return t == t[::-1]

        