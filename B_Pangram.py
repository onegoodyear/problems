import sys
input = sys.stdin.readline

def solve():
    _ = int(input())
    s = set(input().strip().upper())
    print("YES" if len(s) == 26 else "NO")

if __name__ == "__main__":
    solve()