class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        half = self.myPow(x, n//2)
        if n & 1:
            return x * half * half
        return half * half
            
        