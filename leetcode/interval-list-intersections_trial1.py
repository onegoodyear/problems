class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        result = []
        while a < len(firstList) and b < len(secondList):
            lowedge = max(firstList[a][0], secondList[b][0])
            if firstList[a][1] < secondList[b][1]:
                if lowedge <= firstList[a][1]:
                    result.append([lowedge, firstList[a][1]])
                a += 1
            else:
                if lowedge <= secondList[b][1]:
                    result.append([lowedge, secondList[b][1]])
                b += 1
        return result