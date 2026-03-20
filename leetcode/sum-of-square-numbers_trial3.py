import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c & 1:
            for i in range(1,math.floor(math.sqrt(c))+1,2):
                j = math.sqrt(c-i*i)
                if j == int(j): return True
            return False
        else:
            for i in range(math.floor(math.sqrt(c))+1):
                j = math.sqrt(c-i*i)
                if j == int(j): return True
            return False