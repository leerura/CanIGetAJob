import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)


    def bfs(start): 
        visited = [False] *(n+1)
        dist = [0] *(n+1)

        visited[start] = True

        q = deque()
        q.append(start)

        while(q):
            cur = q.popleft()
            for neighbor in adj[cur]:
                if(not visited[neighbor]):
                    visited[neighbor] = True
                    dist[neighbor] = dist[cur] + 1
                    q.append(neighbor)
        
        num = sum(dist)
        return num

    min_count = float('inf')
    min_idx = 0
    for i in range(1,n+1):
        res = bfs(i)
        if(res < min_count):
            min_count = res
            min_idx = i

    print(min_idx)



if __name__ == "__main__":
    solve()