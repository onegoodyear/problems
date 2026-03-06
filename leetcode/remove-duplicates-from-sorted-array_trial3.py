class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[current] = nums[i-1]
                current += 1
        else: nums[current] = nums[len(nums)-1]

        return current + 1
            

        