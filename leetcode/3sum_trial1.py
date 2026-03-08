class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n-2):
            if i == 0 or nums[i-1] != nums[i]:
                j = i + 1
                k = n - 1
                while j < k:
                    sum3 = nums[i] + nums[j] + nums[k]
                    if sum3 > 0:
                        k -= 1
                    elif sum3 < 0:
                        j += 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]: j += 1
                        while j < k and nums[k] == nums[k-1]: k -= 1
                        j += 1
                        k -= 1
        return result
