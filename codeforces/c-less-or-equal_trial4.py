import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    if k == 0:
        if a[0] > 1: print(1)
        else: print(-1)
    elif k == n:
        print(a[-1])
    elif a[k-1] == a[k]: print(-1)
    else: print(a[k-1])
if __name__ == "__main__":
    solve()