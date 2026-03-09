class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        target_reached = False
        n = len(nums)
        diff = 13001
        result = None
        for i in range(n-2):
            if i == 0 or nums[i-1] != nums[i]:
                j = i + 1
                k = n - 1
                while j < k:
                    sum3 = nums[i] + nums[j] + nums[k]
                    diff3 = abs(sum3 - target)
                    if diff3 < diff:
                        diff = min(diff, diff3)
                        result = nums[i] + nums[j] + nums[k]
                    if sum3 > target:
                        k -= 1
                    elif sum3 < target:
                        j += 1
                    else:
                        return target
                    
                    
        return result