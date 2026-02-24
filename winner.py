import math

def escapeGhosts(ghosts: [[int]], target: [int]) -> bool:
    distances = [
        math.sqrt((ghost[0]-target[0])**2 + (ghost[1]-target[1])**2) for ghost in ghosts
    ]
    distance_to_target = math.sqrt(target[0]**2 + target[1]**2)
    ans = any(distance < distance_to_target for distance in distances)
    return ans

print(escapeGhosts([[1,8],[-9,0],[-7,-6],[4,3],[1,3]], [6,-9]))