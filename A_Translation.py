import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()
    if len(s) == len(t):
        print("YES" if all(s[i] == t[len(t)-i-1] for i in range(len(s))) else "NO")
    else: print("NO")

if __name__ == "__main__":
    solve()