import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    has_odd = False
    has_even = False
    for number in a:
        if number & 1:
            has_odd = True
        else: has_even = True


    if has_even and has_odd:
        a.sort()
    
    print(*a)

if __name__ == "__main__":
    solve()