import sys
input = sys.stdin.readline

def solve():
    _ = input()
    print("HARD" if any(map(int, input().split())) else "EASY")


if __name__ == "__main__":
    solve()