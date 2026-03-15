from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        result = 0
        pairs = 0
        n = len(nums)
        d = defaultdict(int)
        left = 0
        for right, curr in enumerate(nums):
            pairs += d[curr]
            d[curr] += 1
            if pairs >= k:
                while left < right and pairs >= k:
                    result += n - right
                    pairs -= (d[nums[left]]-1)
                    d[nums[left]] -= 1
                    left += 1
        return result
                
        
