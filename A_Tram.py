import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    maxCap = 0
    current = 0
    for _ in range(n):
        a, b = map(int, input().split())
        current = current - a + b
        maxCap = max(maxCap, current)
    print(maxCap)



if __name__ == "__main__":
    solve()