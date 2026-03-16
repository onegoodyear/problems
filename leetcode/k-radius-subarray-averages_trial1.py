class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        left = 0
        rightsum = 0
        leftsum = 0
        mid = 0
        while mid < k and mid < n:
            result.append(-1)
            leftsum += nums[mid]
            mid += 1
        right = mid
        while right < mid + k and right < n:
            rightsum += nums[right]
            right += 1
        while mid < n - k :
            result.append((leftsum + rightsum + nums[right])//(2*k+1))
            rightsum += nums[right] - nums[mid]
            right += 1
            leftsum += nums[mid] - nums[left]
            left += 1
            mid += 1
        else:
            while mid < n:
                result.append(-1)
                mid += 1
        return result
            
            