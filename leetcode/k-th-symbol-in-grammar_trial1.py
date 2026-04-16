class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1: return 0
        prev = self.kthGrammar(n-1, (k+1)//2)
        if prev:
            return 1 if k & 1 else 0
        return 0 if k & 1 else 1
        