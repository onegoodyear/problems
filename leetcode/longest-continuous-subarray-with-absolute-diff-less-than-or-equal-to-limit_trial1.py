from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q, max_q = deque(), deque()
        res = 1
        left = 0
        for right, curr in enumerate(nums):
            while min_q and curr < nums[min_q[-1]]:
                min_q.pop()
            min_q.append(right)
            while max_q and curr > nums[max_q[-1]]:
                max_q.pop()
            max_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                if left == max_q[0]: max_q.popleft()
                if left == min_q[0]: min_q.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res