class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        shiftingindex = 0
        counter = 0
        result = 0
        right = 1
        while right < len(s):
            if s[right] == s[right-1]:
                counter += 1
                if counter == 2:
                    result = max(result, right - left)
                    left = shiftingindex
                    counter -= 1
                shiftingindex = right
            right += 1
        else:
            if counter < 2:
                result = max(result, right - left)
        return result