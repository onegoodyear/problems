class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        seen = {s[0]: 0}
        left = 0
        right = 1
        result = 1
        while right < len(s):
            if s[right] in seen and seen[s[right]] >= left:
                result = max(result, right - left)
                left = seen[s[right]] + 1
            seen[s[right]] = right
            right += 1
        else: result = max(result, right - left)
        return result