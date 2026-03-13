class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n: return sum(cardPoints)
        else:
            total = 0
            scores = [0] * (k+1)
            for i in range(k):
                total += cardPoints[i]
                scores[i+1] = total
            total = 0
            index = k - 1
            for j in range(n-1, n - 1 - k , -1):
                total += cardPoints[j]
                scores[index] += total
                index -= 1
            return max(scores)