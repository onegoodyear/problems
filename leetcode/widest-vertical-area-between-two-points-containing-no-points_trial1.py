class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [point[0] for point in points]
        points.sort()
        return max(points[i+1] - points[i] for i in range(len(points)-1))
        