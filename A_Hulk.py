import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    if not n & 1:
        print((n-2)//2 * "I hate that I love that ", "I hate that I love it", sep = "")
    else:
        print((n-1)//2 * "I hate that I love that ", "I hate it", sep = "")
    
    
if __name__ == "__main__":
    solve()