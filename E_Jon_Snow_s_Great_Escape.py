import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        s = input().strip()
        i = 0 
        while True:
            left = (x - 1) - (i + 1)
            right = x - 1 + (i + 1)
            if left >= 0 and right < n:
                if s[left] == "." and s[right] == ".":
                    i += 1
                else: break
            else: break
        if x >= n // 2:
            print(n-x-i+1)
        else:
            print(x-i+1)
if __name__ == "__main__":
    solve()