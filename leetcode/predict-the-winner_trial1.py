class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(turn: bool, left: int, right: int, tot1: int, tot2: int) -> bool:
            if left > right:
                return tot1 >= tot2
            if turn:
                return (
                    helper(not turn, left + 1, right, tot1 + nums[left], tot2)
                    or
                    helper(not turn, left, right - 1, tot1 + nums[right], tot2)
                )
            return (
                helper(not turn, left + 1, right, tot1, tot2 + nums[left])
                and
                helper(not turn, left, right - 1, tot1, tot2 + nums[right])
            )


        return helper(True, 0, len(nums)-1, 0, 0)
        