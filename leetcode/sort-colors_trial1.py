class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        zeros = 0
        twos = 0
        for elem in nums:
            if elem == 0:
                zeros += 1
            elif elem == 1:
                ones += 1
            else: twos += 1
        for i in range(zeros):
            nums[i] = 0
        for i in range(zeros, zeros + ones):
            nums[i] = 1
        for i in range(zeros + ones, len(nums)):
            nums[i] = 2
        