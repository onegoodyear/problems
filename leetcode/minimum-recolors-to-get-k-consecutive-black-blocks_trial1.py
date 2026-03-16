class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = 0
        left = 0
        result = len(blocks)
        for right, curr in enumerate(blocks):
            if curr == "W": counter += 1
            if right - left + 1 == k:
                result = min(result, counter)
                if blocks[left] == "W":
                    counter -= 1
                    left += 1
                else:
                    left += 1
        return result
            


        