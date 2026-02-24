import sys
input = sys.stdin.readline
 
def solve():
    s = input().strip()
    for i in range(len(s)):
        print(" "*i, s[i], sep="")
 
 
 
 
if __name__ == "__main__":
    solve()