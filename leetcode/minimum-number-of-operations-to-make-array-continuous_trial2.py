class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        m = len(nums)
        left = 0
        max_window = 0
        for right in range(m):
            while nums[right] - nums[left] > n - 1:
                left += 1
            max_window = max(max_window, right - left + 1)

        return n - max_window