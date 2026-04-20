class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        min_stack = [0]
        max_stack = [len(nums)-1]
        res = 0
        for i in range(len(nums)):
            if nums[i] < nums[min_stack[-1]]: min_stack.append(i)
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > nums[max_stack[-1]]: max_stack.append(j)
        res = 0
        imax = 0
        while min_stack:
            if nums[max_stack[imax]] >= nums[min_stack[-1]]:
                res = max(res, max_stack[imax] - min_stack[-1])
                min_stack.pop()
            else:
                imax += 1
                if imax == len(max_stack):
                    break
        return res
        
        