class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = set()
        nums[0] %= k
        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i-1]) % k
            if not nums[i] or nums[i] in seen: return True
            seen.add(nums[i-1])
        return False



        
        