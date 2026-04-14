class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n+1)
        def fib2(n: int, dp: [int]) -> int:
            if n == 0 or n == 1: return n
            if not dp[n]:
                dp[n] = fib2(n-1, dp) + fib2(n-2, dp)
            return dp[n]

        return fib2(n, dp)
