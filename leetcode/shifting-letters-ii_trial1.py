class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ords = [ord(ch) - ord('a') for ch in s]
        prefix = [0] * len(s)
        for shift in shifts:
            if shift[2]:
                prefix[shift[0]] += 1
                if shift[1] + 1 < len(s):
                    prefix[shift[1] + 1] -= 1
            else:
                prefix[shift[0]] -= 1
                if shift[1] + 1 < len(s):
                    prefix[shift[1] + 1] += 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        return ''.join(chr((ords[i] + prefix[i]) % 26 + 97) for i in range(len(s)))