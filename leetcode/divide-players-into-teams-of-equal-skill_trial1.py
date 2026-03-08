class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 1
        right = len(skill) - 2
        teamskill = skill[0] + skill[-1]
        result = skill[0] * skill[-1]
        while left < right:
            if skill[left] + skill[right] == teamskill:
                result += skill[left] * skill[right]
            else:
                return -1
            left += 1
            right -= 1
        return result


        