import sys
input = sys.stdin.readline

def solve():
    _, k = map(int, input().split())
    state = input().strip()
    for _ in range(k):
        state = state.replace("BG", "GB")
    print(state)

if __name__ == "__main__":
    solve()