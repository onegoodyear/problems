from collections import deque
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        q = deque()
        for i in range(len(arr)):
            if q:
                if arr[i] == 0:
                    arr[i] = q.popleft()
                    q.append(0)
                    q.append(0)
                else:
                    q.append(arr[i])
                    arr[i] = q.popleft()
            else:
                if arr[i] == 0:
                    q.append(0)
                else: continue
        return arr
        