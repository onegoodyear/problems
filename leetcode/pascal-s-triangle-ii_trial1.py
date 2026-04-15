class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        prev = self.getRow(rowIndex-1)
        temp = 0
        for i in range(1, rowIndex):
            prev[i] += prev[i-1] - temp
            temp = prev[i-1] - temp
        prev.append(1)
        return prev