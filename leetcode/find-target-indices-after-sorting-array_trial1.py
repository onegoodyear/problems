class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        below = 0
        indexes = 0
        for i in range(len(nums)):
            if nums[i] < target:
                below += 1
            elif nums[i] == target:
                indexes += 1
        return [below + j for j in range(indexes)]