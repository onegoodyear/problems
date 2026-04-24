class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def can_cover(r: int) -> bool:
            for house in houses:
                left, right = 0, len(heaters) - 1
                while left <= right:
                    mid = (left+right) // 2
                    if abs(heaters[mid] - house) <= r:
                        break
                    elif heaters[mid] > house:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    return False
            else: return True

        left, right = 0, max(abs(heaters[-1] - houses[0]), abs(houses[-1] - heaters[0]),  houses[-1] - houses[0])
        while left < right:
            mid = (left + right) // 2
            if can_cover(mid):
                right = mid
            else:
                left = mid + 1
        return left