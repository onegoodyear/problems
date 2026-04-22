class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left, right = 1, x
        while left < right:
            mid = left + (right - left + 1) // 2
            temp = mid * mid
            if temp > x:
                right = mid - 1
            elif temp < x:
                left = mid
            else: return mid

        return left
        