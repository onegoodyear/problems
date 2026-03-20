class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k = k % len(nums)
        for left in range(k//2):
            nums[left], nums[k-1-left] = nums[k-1-left], nums[left]
        for left in range((len(nums)-k)//2):
            nums[k+left], nums[len(nums)-1-left] = nums[len(nums)-1-left], nums[k+left]


