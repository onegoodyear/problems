class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = None
        result = 0
        left = 0
        right = 0
        while right < len(arr) - 1:
            if arr[right] > arr[right+1]:
                sign = True
                left = right
                break
            elif arr[right] < arr[right+1]:
                sign = False
                left = right
                break
            else:
                right += 1
                left = right
        while right < len(arr) - 1:
            if sign:
                if arr[right] > arr[right+1]:
                    right += 1
                    sign = False
                elif arr[right] < arr[right+1]:
                    result = max(result, right-left+1)
                    left = right
                    right += 1
                    sign = True
                else:
                    result = max(result, right-left+1)
                    while right < len(arr) - 1:
                        if arr[right] > arr[right+1]:
                            sign = True
                            left = right
                            break
                        elif arr[right] < arr[right+1]:
                            sign = False
                            left = right
                            break
                        else: 
                            right += 1
                            left = right        
            else:
                if arr[right] > arr[right+1]:
                    result = max(result, right-left+1)
                    left = right
                    right += 1
                    sign = False
                elif arr[right] < arr[right+1]:
                    right += 1
                    sign = True
                else:
                    result = max(result, right-left+1)
                    while right < len(arr) - 1:
                        if arr[right] > arr[right+1]:
                            sign = True
                            left = right
                            break
                        elif arr[right] < arr[right+1]:
                            sign = False
                            left = right
                            break
                        else:
                            right += 1
                            left = right
        return max(result, right - left + 1)