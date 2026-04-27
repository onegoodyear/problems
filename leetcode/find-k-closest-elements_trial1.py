class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        mid = None
        while left <= right:
            mid = (right + left) // 2
            if arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                right = mid - 1
            else:
                break
        left = min(mid-k, 0)
        return arr[left: mid+1]
