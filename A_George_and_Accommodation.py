import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    ans = 0
    for _ in range(n):
        p, q = map(int, input().split())
        if q - p > 1: ans += 1
    print(ans)

if __name__ == "__main__":
    solve()