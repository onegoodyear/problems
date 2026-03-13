class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        seen = set()
        total = 0
        for right, num in enumerate(nums):
            total += num
            if right - left + 1 == k:
                if num in seen:
                    while left < right and nums[left] != num:
                        seen.remove(nums[left])
                        total -= nums[left]
                        left += 1
                    else: 
                        total -= nums[left]
                        left += 1
                else:
                    result = max(result, total)
                    total -= nums[left]
                    seen.add(num)
                    seen.remove(nums[left])
                    left += 1
            else:
                if num in seen:
                    while left < right:
                        if nums[left] != num:
                            seen.remove(nums[left])
                            total -= nums[left]
                            left += 1
                        else:
                            break
                    total -= nums[left]
                    left += 1
                else:
                    seen.add(num)

        return result