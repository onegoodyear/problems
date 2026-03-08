class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_left = 0

        for ch in s:
            if ch == t[t_left]:
                t_left += 1
            
            if t_left == len(t):
                break 

        return len(t) - t_left
        