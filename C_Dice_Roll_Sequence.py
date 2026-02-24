import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = map(int, input().split())
        ans = 0
        prev = 0
        temp = 0
        while True:
            try:
                f1 = next(a)
                f2 = next(a)
                temp = f2
                if f1 == f2 or f1 + f2 == 7:
                    ans += 1
                    temp = 0
                    prev = 0
                elif f1 == prev or f1 + prev == 7:
                    ans += 1
                prev = f2
            except StopIteration:
                if f1 != StopIteration:
                    if temp == f1 or temp + f1 == 7:
                        ans += 1
                break
        print(ans)


if __name__ == "__main__":
    solve()