import sys
input = sys.stdin.readline

def solve():
    w, t = map(int, input().split())
    n = int(input())
    for _ in range(n):
        wi, ti = map(int, input().split())
        if wi > w:
            print("The Fallen Champion")
            break
        elif wi == w:
            if ti < t:
                print("The Fallen Champion")
                break
    else: print("The Champion Saves the Accused")

if __name__ == "__main__":
    solve()