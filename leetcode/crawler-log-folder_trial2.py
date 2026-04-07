class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == "../": res = max(res-1, 0)
            elif log == "./": continue
            else: res += 1
        return res
        