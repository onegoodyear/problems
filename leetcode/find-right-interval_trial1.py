from bisect import bisect_left
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        starts = [(intervals[i][0], i) for i in range(len(intervals))]
        starts.sort()
        for i in intervals:
            j = bisect_left(starts, (i[1], -1))
            if 0 <= j < len(intervals): res.append(starts[j][1])
            else: res.append(-1)
        return res