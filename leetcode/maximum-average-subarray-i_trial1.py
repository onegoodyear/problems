class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k
        sumk = sum(nums[i] for i in range(left, right))
        result = sumk
        while right < n:
            sumk -= nums[left]
            left += 1
            sumk += nums[right]
            right += 1
            result = max(sumk, result)
        return result / k