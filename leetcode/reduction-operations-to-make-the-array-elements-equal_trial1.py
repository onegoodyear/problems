class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        steps = 0
        result = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[j] != nums[i]: 
                    break
                j += 1    
            result += steps * (j - i)
            i = j
            steps += 1
        return result