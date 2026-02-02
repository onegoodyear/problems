import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    print("Anton" if s.count("A") > n//2 else "Friendship" if s.count("A") == (n + 1) // 2 else "Danik")

if __name__ == "__main__":
    solve()