class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap: int) -> bool:
            days_needed = 1
            curr = 0
            for w in weights:
                if curr + w > cap:
                    curr = 0
                    days_needed += 1
                curr += w
            return days_needed <= days
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left