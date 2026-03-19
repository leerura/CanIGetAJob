import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b = map(int, input().split())
        adj[b].append(a)
    

    def bfs(start):
        answer = 1
        visited = [False]*(n+1)
        visited[start]=True
        q = deque()
        q.append(start)

        while(q):
            cur = q.popleft()
        
            for neighbor in adj[cur]:
                if(not visited[neighbor]):    
                    visited[neighbor] = True
                    q.append(neighbor)
                    answer += 1
        return answer
    
    result = []
    max_count = 0
    
    for i in range(1,n+1):
        res = bfs(i)
        if(res> max_count):
            max_count = res
            result = [i]
        elif(res==max_count):
            result.append(i)
    
    print(*(result))


                


if __name__ == "__main__":
    solve()