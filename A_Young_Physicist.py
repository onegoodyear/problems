import sys
input = sys.stdin.readline

def solve():
    sum = [0, 0, 0]
    for x, y, z in (map(int, input().split()) for _ in range(int(input()))):
        sum[0] += x
        sum[1] += y
        sum[2] += z
    print("YES" if sum == [0, 0, 0] else "NO")


if __name__ == "__main__":
    solve()