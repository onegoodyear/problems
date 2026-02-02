import sys
input = sys.stdin.readline

def solve():
    key = input().strip()
    n = int(input())
    firstLetterFoundInSecondPos = False
    secondLetterFoundInFirstPos = False
    for _ in range(n):
        s = input().strip()
        if s[1] == key[0]:
            firstLetterFoundInSecondPos = True
        if s[0] == key[1]:
            secondLetterFoundInFirstPos = True
        if s == key or (secondLetterFoundInFirstPos and firstLetterFoundInSecondPos):
            print("YES")
            break
    else: print("NO")

if __name__ == "__main__":
    solve()