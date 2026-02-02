import sys
input = sys.stdin.readline

def solve():
    n = input().strip()
    cnt = str(n.count("4") + n.count("7"))
    print("YES" if set(cnt) <= {"4", "7"} else "NO")

if __name__ == "__main__":
    solve()