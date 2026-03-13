from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        t_frq = Counter(t)
        s_frq = defaultdict(int)
        min_len = float('inf')
        result = ""
        for right, ch in enumerate(s):
            s_frq[ch] += 1
            valid = True
            for k, v in t_frq.items():
                if s_frq[k] < v:
                    valid = False
                    break
            while left <= right and valid:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left: right + 1]
                s_frq[s[left]] -= 1
                if s[left] in t_frq and s_frq[s[left]] < t_frq[s[left]]:
                    valid = False
                left += 1


        return result