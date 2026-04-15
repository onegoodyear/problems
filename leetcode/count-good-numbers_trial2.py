class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def power_with_mod(a, b):
            res = 1
            while b:
                if b & 1:
                    res = res * a % mod
                a = a * a % mod
                b //= 2
            return res
        five_pow = (n+1) // 2
        four_pow = n // 2

        return power_with_mod(4, four_pow) * power_with_mod(5, five_pow) % mod
                