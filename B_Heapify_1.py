import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    powers =  {
    1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
    1024, 2048, 4096, 8192, 16384, 32768,
    65536, 131072
}
    for _ in range(t):
        n = int(input())
        permutation = list(map(int, input().split()))
        for i in range(1, n+1):
            if not (
                (permutation[i-1] % i == 0 and (permutation[i-1] // i) in powers)
                    or
                (i % permutation[i-1] == 0 and (i // permutation[i-1]) in powers)
            ):
                print("NO")
                break
        else: print("YES")

if __name__ == "__main__":
    solve()