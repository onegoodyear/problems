import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    responses =  [0, 5, 2, 3, 4, 1, 6, 1, 4, 3, 2, 5]
    for _ in range(t):
        n = int(input())
        print(responses[n%12])


if __name__ == "__main__":
    solve()