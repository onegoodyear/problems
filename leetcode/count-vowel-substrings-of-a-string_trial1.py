class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        res = 0
        n = len(word)
        for left in range(n):
            freq = {}
            right = left
            while right < n and word[right] in vowels:
                freq[word[right]] = freq.get(word[right], 0) + 1
                if len(freq) == 5:
                    res += 1
                right += 1

        return res