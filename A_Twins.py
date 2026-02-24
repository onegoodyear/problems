import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    index = 1
    me = coins[-index]
    while me <= sum(coins) // 2:
        index += 1
        me += coins[-index]
    
    print(index)

if __name__ == "__main__":
    solve()