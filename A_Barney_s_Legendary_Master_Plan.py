import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted(map(int, input().split()))
        i = 0
        ans = 0
        while i < len(a):
            offset = a[i]
            for j in range(i, len(a)):
                a[j] -= offset
                if a[j] <= 0: 
                    i = j + 1
            ans += 2
        print(ans-1)
if __name__ == "__main__":
    solve()