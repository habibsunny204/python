import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    v = input().strip()

    ans = 0 
    i = 0
    while i < n:
        if v[i] == "1":
            i += k
        else:
            ans += 1
        i += 1

    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
