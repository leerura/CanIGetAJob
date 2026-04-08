import sys

from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input().strip())
    times = [0]*(n+1)
    degrees = [0]*(n+1)

    adj = [[] for _ in range(n+1)]
    rev_adj = [[] for _ in range(n+1)]
    
    
    for i in range(n):
        data = list(map(int,input().split()))

        times[i+1] = data[0]
        length = len(data)-2

        degrees[i+1] = length

        for j in range(1,length+1):
            adj[data[j]].append(i+1)
            rev_adj[i+1].append(data[j])

    q = deque()

    for i in range(1,n+1):
        if(degrees[i]==0):
            q.append(i)

    
    dp = [0] * (n+1)

    while(q):
        cur = q.popleft()

        for precessor in rev_adj[cur]:
            dp[cur] = max(dp[cur], dp[precessor]+times[precessor])

        for next in adj[cur]:
            degrees[next] = degrees[next]-1

            if(degrees[next]==0):
                q.append(next)

    for i in range(1,n+1):
        print(dp[i]+times[i])

if __name__=="__main__":
    solve()