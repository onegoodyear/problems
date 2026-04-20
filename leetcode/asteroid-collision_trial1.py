class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rs = []  # right_stack
        ls = []  # left_stack
        for i, a in enumerate(asteroids):
            if a > 0: rs.append(a)
            else:
                while rs and rs[-1] < abs(a):
                    rs.pop()
                if rs and rs[-1] == abs(a):
                    rs.pop()
                    continue
                if not rs: ls.append(a)
        return ls+rs