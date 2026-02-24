import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    i = 0
    for ch in s:
        if ch == "hello"[i]: i += 1
        if i > 4:
            print("YES")
            break
    else: print("NO")

if __name__ == "__main__":
    solve()