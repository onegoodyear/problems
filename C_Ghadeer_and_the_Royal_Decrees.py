import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        maximum = max(a)
        output = ""
        for _ in range(m):
            c, l, r = input().split()
            l = int(l)
            r = int(r)
            if l <= maximum and maximum <= r:
                if c == "-":
                    maximum -= 1
                else:
                    maximum += 1
            output += str(maximum) + " "
        print(output)

if __name__ == "__main__":
    solve()