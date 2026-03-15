class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        total = 0
        result = 0

        for right, num in enumerate(nums):
            while num in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1

            seen.add(num)
            total += num
            result = max(result, total)

        return result
        