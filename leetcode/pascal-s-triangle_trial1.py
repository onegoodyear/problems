class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        prev = self.generate(numRows-1)
        prev.append([1])
        for i in range(numRows-2):
            prev[-1].append(prev[-2][i] + prev[-2][i+1])
        prev[-1].append(1)
        return prev