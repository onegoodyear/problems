import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    caps = 0
    for ch in s:
        if ord(ch) < 92:
            caps += 1
        else: caps -= 1
    if caps > 0: print(s.upper())
    else: print(s.lower())


if __name__ == "__main__":
    solve()