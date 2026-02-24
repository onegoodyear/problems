import sys
input = sys.stdin.readline

def solve():
    for _ in int(input()):
        n = int(input())
        coins = map(int, input().split())
        odd = filter(lambda x: x&1, coins)
        even = filter(lambda x: not x&1, coins)
        even.sort()
        odd.sort()
        res = {}
        tot = sum(coins)
        res[n] = tot if tot&1 else 0
        for i in range(n-1, 0, -1):
            


if __name__ == "__main__":
    solve()