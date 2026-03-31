import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    adj = [[] for _ in range(n+1)]

    for _ in range(n-1):
        v1, v2, e = map(int,input().split())
        adj[v1].append((v2,e))
        adj[v2].append((v1,e))

    def dfs(start):
        
        dist = [-1] * (n+1)

        dist[start] = 0


        q = deque()
        q.append(start)

        while(q):
            cur = q.popleft()

            for next,edge in adj[cur]:
                if(dist[next] == -1):
                    dist[next] = dist[cur] + edge
                    q.append(next)


        max_vertex = 0
        max_distance = 0
        for i in range(1,n+1):
            if dist[i] > max_distance:
                max_distance = dist[i]
                max_vertex =i



        return max_vertex, max_distance
    
    a,_ = dfs(1)
    _,answer = dfs(a)

    print(answer)



if __name__=="__main__":
    solve()