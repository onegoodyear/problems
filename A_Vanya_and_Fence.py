import sys
input = sys.stdin.readline

def solve():
    n, h = map(int, input().split())
    s = map(int, input().split())
    print(sum(2 if a > h else 1 for a in s))


if __name__ == "__main__":
    solve()