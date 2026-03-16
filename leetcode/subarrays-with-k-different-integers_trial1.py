class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        seen = set()
        lastindex = {}
        result = 0
        left =  0
        for right, curr in enumerate(nums):
            seen.add(curr)
            lastindex[curr] = right
            if len(seen) > k:
                min_key = min(lastindex, key = lastindex.get)
                left = lastindex[min_key] + 1
                seen.remove(min_key)
                del lastindex[min_key]
            if len(seen) == k:
                result += min(lastindex.values()) - left + 1
        return result
        