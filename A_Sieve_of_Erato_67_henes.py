import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("YES" if 67 in map(int, input().split()) else "NO")

if __name__ == "__main__":
    solve()