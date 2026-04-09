class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i, c in enumerate(nums):
            while stack and nums[stack[-1]] < c:
                res[stack.pop()] = c
            stack.append(i)
        for i in range(stack[0]+1):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
        return res
                
