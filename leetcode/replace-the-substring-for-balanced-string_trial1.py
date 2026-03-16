from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        frq = Counter(s)
        target = len(s) // 4
        result = len(s)
        left = 0
        if all(frq[c] == target for c in "QWER"): return 0
        for right, curr in enumerate(s):
            frq[curr] -= 1
            while left < len(s) and all(frq[c] <= target for c in "QWER"):
                result = min(result, right - left + 1)
                frq[s[left]] += 1
                left += 1
        return result