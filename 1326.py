import sys
from collections import deque
"""
이 문제 좋다... 처음에 그리디인 거 같다가도...? 알고보니 BFS인...
최소 점프 횟수
"""
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    bridge = list(map(int, input().split()))
    start, end = map(int, input().split())

    visited = [False] * (n+1)
    dist = [0]*(n+1)


    if (start==end): return 0


    visited = [False] * (n+1)
    dist = [0]*(n+1)

    def bfs(start):
        visited[start] = True

        q = deque()
        q.append(start)

        while(q):
            cur = q.popleft()

            jump = bridge[cur-1]
            next_right = cur + jump
            next_left = cur - jump

            while next_right <= n:
                if(not visited[next_right]):
                    visited[next_right] =True
                    dist[next_right] = dist[cur] + 1
                    q.append(next_right)
                next_right += jump 
            
            while  1<= next_left:
                if(not visited[next_left]):
                    visited[next_left] =True
                    dist[next_left] = dist[cur] + 1
                    q.append(next_left)
                next_left -= jump 

    bfs(start)
    print(dist[end] if dist[end] != 0 else -1)

if __name__=="__main__":
    solve()
