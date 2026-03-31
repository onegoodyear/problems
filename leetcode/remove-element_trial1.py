class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                while right >= left and nums[right] == val: right -= 1
                if right < left: break
                nums[left] = nums[right]
                right -= 1
            left += 1
        return left
        