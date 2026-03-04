class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp1 = min(nums)
        max2 = temp1
        max1 = max(nums)
        for number in nums:
            if number >= max2 and number != max1:
                max2 = number
        if max2 == temp1: return max1
        max3 = min(nums)
        for number in nums:
            if number >= max3 and number != max1 and number != max2:
                max3 = number
        return max1 if max3 == max2 else max3
        