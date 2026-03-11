from collections import defaultdict, Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        freq = Counter(p)
        seen = defaultdict(int)
        result = []
        while right < len(s):
            if right - left == len(p):
                if seen == freq:
                    result.append(left)                
                seen[s[left]] -= 1
                if seen[s[left]] == 0: del seen[s[left]]
                left += 1
            if s[right] in freq:
                seen[s[right]] += 1
            else: 
                seen.clear()
                left = right + 1
            right += 1
        else:
            if right - left == len(p) and seen == freq:
                result.append(left)
        return result
        