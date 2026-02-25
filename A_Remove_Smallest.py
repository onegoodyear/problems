import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        print("NO" if any(arr[i+1] - arr[i] > 1 for i in range(n-1)) else "YES")

if __name__ == "__main__":
    solve()