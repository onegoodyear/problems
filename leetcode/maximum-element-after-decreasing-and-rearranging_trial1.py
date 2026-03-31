class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        next = 1
        for i in range(1, len(arr)):
            if arr[i] > next:
                arr[i] = next
                next += 1       
        return next

        