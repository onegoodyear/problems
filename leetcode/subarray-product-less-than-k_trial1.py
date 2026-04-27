class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        result = 0
        for right, curr in enumerate(nums):
            product *= curr
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            result += right - left + 1
        return result
        