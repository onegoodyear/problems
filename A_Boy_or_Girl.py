import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    if len(set(s)) & 1: print("IGNORE HIM!")
    else: print("CHAT WITH HER!")

if __name__ == "__main__":
    solve()