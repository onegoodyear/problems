from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1frq = Counter(s1)
        s2frq = defaultdict(int)
        left = 0
        for right, curr in enumerate(s2):
            if curr in s1frq:
                s2frq[curr] += 1
                if s2frq[curr] > s1frq[curr]:
                    while left < right and s2frq[curr] > s1frq[curr]:
                            s2frq[s2[left]] -= 1
                            left += 1
                if right - left == len(s1) - 1 and s1frq == s2frq:
                        return True
            else:
                left = right + 1
                s2frq.clear()
        return False