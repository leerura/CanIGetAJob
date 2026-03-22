import sys

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    adj = [[] for _ in range(n+1)]
    for i in range(5):
        tmp = list(map(int, input().split()))
        m = tmp[0]

        for k in range(m):
            adj[i+1].append(tmp[k+1])

    print(adj)


if __name__=="__main__":
    solve()