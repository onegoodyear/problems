class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find left
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if not nums or nums[left] != target:
            return [-1, -1]

        ans = [left, None]

        # find right
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        ans[1] = left
        return ans
