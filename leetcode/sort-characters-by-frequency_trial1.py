from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        sorted_keys = sorted(d, key = lambda k: -d[k])
        result = ""
        for k in sorted_keys:
            result += k * d[k]
        return result