import sys
input = sys.stdin.readline


def solve():
    n = int(input())
    luckys = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    for lucky in luckys:
        if lucky <= n:
            if not n % lucky:
                print("YES")
                break
        else:
            print("NO")
            break
    else: print("NO")
if __name__ == "__main__":
    solve()