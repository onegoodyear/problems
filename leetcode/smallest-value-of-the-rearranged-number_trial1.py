class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            result = ""
            digits = [0] * 10
            for ch in str(num):
                digits[ord(ch)-ord('0')] += 1
            min = ""
            much = 0
            index = 10
            for i in range(1, 10):
                if digits[i] != 0:
                    min = str(i)
                    much = digits[i]
                    index = i + 1
                    break
            result += min * 1
            result += '0' * digits[0]
            result += min * (much - 1)
            for i in range(index, 10):
                result += str(i) * digits[i]
            return int(result)
        else:
            num = -num
            result = ""
            digits = [0] * 10
            for ch in str(num):
                digits[ord(ch)-ord('0')] += 1
            for i in range(9, -1, -1):
                result += str(i) * digits[i]
            return -int(result)