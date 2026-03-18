import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, v = map(int,input().split())
    edges = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    for edge in edges:
        edge.sort()
    
    d_visited = [False] * (n+1)
    d_result = []

    b_visited = [False] * (n+1)
    b_result =[]

    def dfs(start):
        nonlocal d_visited
        nonlocal d_result
        d_result.append(start)

        d_visited[start] = True

        for near in edges[start]:
            if not d_visited[near]:
                dfs(near)
    dfs(v)

    def bfs(start):
        nonlocal b_visited
        nonlocal b_result

        q = deque()

        b_visited[start] = True

        q.append(start)
        b_result.append(start)

        while(q):
            cur = q.popleft()

            for near in edges[cur]:
                if not b_visited[near]:
                    b_visited[near] = True
                    b_result.append(near)
                    q.append(near)
        
    bfs(v)


    print(*(d_result))
    print(*(b_result))
    

if __name__ == "__main__":
    solve()