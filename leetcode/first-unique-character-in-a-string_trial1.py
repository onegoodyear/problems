from collections import deque, defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        q = deque()
        for i, c in enumerate(s):
            freq[c] += 1
            q.append(i)
            while q and freq[s[q[0]]] > 1:
                q.popleft()
        return q[0] if q else -1