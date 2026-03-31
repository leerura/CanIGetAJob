import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solve():
    v = int(input().strip())

    adj = [[] for _ in range(v+1)]
    
    #얘부터가 v*v/2 시간 복잡돈데... 흠 일단 푸는 거 먼저 집중해보자
    for i in range(v):
        data = list(map(int,input().split()))
        v1 = data[0]
        for j in range(1, len(data) - 1, 2):
            v2 = data[j]
            edge = data[j+1]
            adj[v1].append((v2, edge))

    #dfs 모두적용

    def bfs(start_node):
        dist = [-1] * (v+1)
        dist[start_node] = 0

        visited = [False] * (v+1)
        visited[start_node] = True

        q = deque()
        q.append(start_node)

        while(q):
            cur = q.popleft()

            for next, edge in adj[cur]:
                if(not visited[next]):
                    visited[next] = True
                    dist[next] = dist[cur] + edge
                    q.append(next)

        max_dist = 0
        max_node = 0

        for i in range(1,v+1):
            if(dist[i] > max_dist):
                max_node = i
                max_dist = dist[i]

        return max_node, max_dist
    
    a, _ = bfs(1)
    b, answer = bfs(a)

    print(answer)






    

if __name__=="__main__":
    solve()