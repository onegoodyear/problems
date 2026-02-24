import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        clocks = list(map(int, input().split()))
        for i in range(len(clocks)):
            if clocks[i] < 2 * (n-i) - 1 or clocks[i] <= 2 * i :
                print("NO")
                break
        else: print("YES")
        

if __name__ == "__main__":
    solve()