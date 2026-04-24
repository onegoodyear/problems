class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        down, up = 0, len(matrix) - 1
        row = None
        while down <= up:
            mid = (down + up) // 2
            if target < matrix[mid][0]:
                up = mid - 1
            elif target > matrix[mid][-1]:
                down = mid + 1
            else:
                row = mid 
                break
        else: return False
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False

        