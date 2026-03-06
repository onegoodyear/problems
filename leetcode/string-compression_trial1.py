class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        result = ""
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                counter += 1
            else:
                if counter > 1:
                    result += chars[i-1] + str(counter)
                else:
                    result += chars[i-1]
                counter = 1
        if counter > 1: result += chars[-1] + str(counter)
        else: result += chars[-1]
        for i in range(len(result)):
            if i < len(chars):
                chars[i] = result[i]
            else:
                chars.append(result[i])
        return len(result)