class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        position = {}
        for i in range(len(arr)):
            position[arr[i]] = i
        flips = []
        for j in range(1, len(arr)+1):
            pos = position[j]
            for flip in flips:
                if pos < flip:
                    pos = flip-1-pos
            if pos == 0:
                flips.append(len(arr)+1-j)
            elif pos == len(arr) - j:
                continue
            else:
                flips.append(pos+1)
                flips.append(len(arr)+1-j)
        flips.append(len(arr))
        return flips