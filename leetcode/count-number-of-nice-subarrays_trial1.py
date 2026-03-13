from collections import deque
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        q = deque()
        left = 0
        result = 0
        for right, curr in enumerate(nums):
            if curr & 1:
                q.append(right)
            if len(q) == k:
                result += q[0] - left + 1
            elif len(q) > k:
                left = q.popleft() + 1
                result += q[0] - left + 1
        return result
