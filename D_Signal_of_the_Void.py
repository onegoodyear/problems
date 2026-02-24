import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        residents = list(zip(a, b))
        residents.sort(key=lambda x: (x[1], -x[0]))
        print(residents)
        

if __name__ == "__main__":
    solve()