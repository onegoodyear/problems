class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        onetime = False
        while left < right:
            if s[left] != s[right]:
                l = left + 1
                r = right
                while l < r:
                    if s[l] != s[r]: break
                    r -= 1
                    l += 1
                else: return True
                l = left
                r = right - 1
                while l < r:
                    if s[l] != s[r]: break
                    r -= 1
                    l += 1
                else: return True
                break
            left += 1
            right -= 1
        else: return True
        return False

        
        
        