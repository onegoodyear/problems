class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseStringRec(s: List[str], beg: int, end: int) -> None:
            if beg < end:
                s[beg], s[end] = s[end], s[beg]
                reverseStringRec(s, beg + 1, end - 1)
        reverseStringRec(s, 0, len(s)-1)

        