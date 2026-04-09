from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        table_right = {}
        stack = []
        n = len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                table_right[stack.pop()] = i
            stack.append(i)
        stack = []
        table_left = {}
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                table_left[stack.pop()] = i
            stack.append(i)
        res =  0
        for i in range(len(heights)):
            res = max(res, (table_right.get(i, n) - table_left.get(i, -1) - 1)  * heights[i])
        return res