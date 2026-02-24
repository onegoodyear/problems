import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        candies = sorted(map(int, input().split()))
        avg = sum(candies) // n
        if avg !=  sum(candies) / n:
            print(-1)
            continue
        k = 0
        while n - k > 0:
            if candies[-k-1] > avg:
                k += 1
            else: break
        print(k)
            
    print()
if __name__ == "__main__":
    solve()