import sys
input = sys.stdin.readline


def solve():
    _ = int(input())
    rocks = list(map(int, input().split()))
    rocks.sort()
    waiting = rocks[0]
    reminder = 0
    for i in range(1, len(rocks)):
        if waiting < 0:
            print(-1)
            break
        reminder += rocks[i] - rocks[i-1]
        if rocks[i] == rocks[i-1]:
            if reminder < 1:
                waiting -= 1
            else: reminder -= 1
    else: print(waiting)
if __name__ == "__main__":
    solve()