import sys
import math
input = sys.stdin.readline

def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        healths = list(map(int, input().split()))
        points = list(map(int, input().split()))
        monsters = [[abs(points[i]), healths[i]] for i in range(n)]
        monsters.sort(key = lambda x: x[0])
        rounds = 0
        reminder = 0
        for monster in monsters:
            monster[0] -= rounds
            if monster[1] > reminder:
                monster[1] -= reminder
                reminder = 0
            else:
                reminder -= monster[1]
                monster[1] = 0
            if monster[0] >= math.ceil(monster[1]/k):
                rounds += math.ceil(monster[1]/k)
                reminder += rounds * k - monster[1]
            else:
                print("NO, Rounds =", rounds)
                break
        else: print("YES, Rounds =", rounds)

if __name__ == "__main__":
    solve()