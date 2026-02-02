import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    for _ in range(k):
        if n % 10:
            n -= 1
        else: 
            n //= 10
    print(n)


if __name__ == "__main__":
    solve()
