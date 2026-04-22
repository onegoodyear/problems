class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(n: int) -> bool:
            return sum((pile + n - 1) // n for pile in piles) <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1
        return left