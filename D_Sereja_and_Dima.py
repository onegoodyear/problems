import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    cards = list(map(int, input().split()))
    sereja = dema = 0
    turn = True
    left = 0
    right = n - 1
    while(left <= right):
        if (cards[left] < cards[right]):
            if turn:
                sereja += cards[right]
            else: dema += cards[right]
            right -= 1
        else:
            if turn:
                sereja += cards[left]
            else: dema += cards[left]
            left += 1
        turn = not turn
    print(sereja, dema)

if __name__ == "__main__":
    solve()