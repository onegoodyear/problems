from collections import defaultdict
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        counter = 0
        left = 0
        result = 0
        for right, ch in enumerate(s):
            if ch in vowels:
                counter += 1
            if right - left < k:
                result = max(result, counter)
            else:
                if s[left] in vowels:
                    counter -= 1
                    left += 1
                while left <= right:
                    if s[left] in vowels:
                        result = max(result, counter)
                        break
                    left += 1
        else:
            result = max(result, counter)
        return result

        