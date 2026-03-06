class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = [(score[i], i) for i in range(len(score))]
        temp.sort(key = lambda x: -x[0])
        score[temp[0][1]] = "Gold Medal"
        if len(temp) > 1:
            score[temp[1][1]] = "Silver Medal"
            if len(temp) > 2:
                score[temp[2][1]] = "Bronze Medal"
                for i in range(3, len(score)):
                    score[temp[i][1]] = str(i+1)
        return score
        