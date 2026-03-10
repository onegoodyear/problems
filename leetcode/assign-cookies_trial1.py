class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gp = 0
        result = 0
        for size in s:
            if gp < len(g) and size >= g[gp]:
                result += 1
                gp += 1
        return result
        