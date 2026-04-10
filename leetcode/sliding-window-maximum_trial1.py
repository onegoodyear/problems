from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        left = 0
        for right, curr in enumerate(nums):
            while q and q[-1] < curr:
                q.pop()
            q.append(curr)
            if right - left + 1 == k: 
                res.append(q[0])
                if nums[left] == q[0]:
                    q.popleft()
                left += 1
        return res

