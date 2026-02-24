import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        perm = [0 for _ in range(n)]
        stop = False
        for i in range(n):
            deck = list(map(int, input().split()))
            modulo = deck[0] % n
            if all(card % n == modulo for card in deck) and perm[modulo] == 0:
                perm[modulo] = i + 1
            else: 
                stop = True
        if stop: print(-1)
        else: print(*perm)
       
        

if __name__ == "__main__":
    solve()