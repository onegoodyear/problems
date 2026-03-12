class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        d = {}
        for right, fruit in enumerate(fruits):
            if fruit in d:
                d[fruit] += 1
            else:
                if len(d) < 2:
                    d[fruit] = 1
                else:
                    result = max(result, right - left)
                    while left < right:
                        d[fruits[left]] -= 1
                        if d[fruits[left]] == 0:
                            del d[fruits[left]]
                            d[fruit] = 1
                            break
                        left += 1
                    left += 1
        else: 
            result = max(result, right - left + 1)
        return result

