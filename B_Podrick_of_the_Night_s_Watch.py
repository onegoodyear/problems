import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    ravens = defaultdict(int)
    for _ in range(n):
        m = int(input())
        for _ in range(m):
            s, h = input().split()
            ravens[(s,h)] += 1
    print("YES" if max(ravens.values()) / n >= 0.8 else "NO")

if __name__ == "__main__":
    solve()