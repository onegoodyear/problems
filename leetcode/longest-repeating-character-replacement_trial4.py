from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = 0
        main = s[0]
        result = 1
        d = defaultdict(int)
        for right, ch in enumerate(s):
            if ch != main:
                counter += 1
            d[ch] += 1
            if counter > k:
                result = max(result, right - left)
                while left <= right:
                    if s[left] != main:
                        main = s[left]
                        counter = (right - left + 1) - d[main]
                        break
                    else: d[main] -= 1
                    left += 1
        else:
            max_key = max(d, key=d.get)
            counter = right - left + 1 - d[max_key]
            result = max(result, right - left + 1 + min(left, k - counter))
        return result
                

            
