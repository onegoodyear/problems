import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    print("YES" if "1111111" in s or "0000000" else "NO")

if __name__ == "__main__":
    solve()