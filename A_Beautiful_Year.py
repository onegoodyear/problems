import sys
input = sys.stdin.readline

def solve():
    for i in range(int(input())+1, 9876):
        if len(set(str(i))) == 4: 
            print(i)
            break
    

if __name__ == "__main__":
    solve()