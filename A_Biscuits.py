import sys
import math
input = sys.stdin.readline

def solve():
    t = int(input())
    for i in range(t):
        n = int(input())
        if n < 3: 
            print(0)
        elif n&1:
            print(n//2)
        else:
            print((n-2)//2)



if __name__ == "__main__":
    solve()