import sys
from collections import deque


input = sys.stdin.readline

def solve():
    n = int(input().strip())

    adj = [[] for _ in range(n+1)]

    for i in range(n):
        line = list(map(int, input().split()))
        count = line[0]

        for j in range(count):
            adj[i+1].append(line[j+1])

    blue = []
    white = []

    
    visited = [False] *(n+1)
    
    def bfs(start):

        blue.append(start)

        q = deque()
        q.append((start,"blue"))

        visited[start] = True

        while(q):
            cur,cur_color = q.popleft()

            for next in adj[cur]:
                if(not visited[next]):
                    visited[next] = True
                    color = "white" if cur_color=="blue" else "blue"
                    if(color=="white"):
                        white.append(next)
                    else:
                        blue.append(next)

                    q.append((next,color))

    for i in range(1,n+1):
        if(not visited[i]):
            bfs(i)

    blue.sort()
    white.sort()

    print(len(blue))
    print(*(blue))
    print(len(white))
    print(*(white))

if __name__=="__main__":
    solve()