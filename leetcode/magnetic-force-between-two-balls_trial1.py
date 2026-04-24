from bisect import bisect_left
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def can_distribute(force: int) -> bool:
            i = 0
            counter = 1
            while counter < m:
                i = bisect_left(position, position[i] + force)
                if i == n: return False
                else: counter += 1
            return True
        
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if can_distribute(mid):
                left = mid
            else:
                right = mid - 1
        return left
