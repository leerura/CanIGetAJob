import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n,m = map(int,input().split()) #n: 섬개수, m: 다리 개수

    adj = [[] for _ in range(n+1)]

    weights = []

    for _ in range(m):
        u,v,w = map(int, input().split())

        adj[u].append((v,w))
        adj[v].append((u,w))

        weights.append(w)

    a,b = map(int, input().split())

    weights.sort()


    def dfs(start,end,w):
        visited = [False] *(n+1)

        q = deque()

        visited[start] = True
        q.append(start)

        
        while(q):
            cur = q.popleft()

            for next, weight in adj[cur]:
                if(not visited[next] and w<=weight):
                    visited[next] = True
                    q.append(next)





        return visited[end]


    left = 0
    right = len(weights)-1

    answer = left+(right-left)//2
    while(left<=right):
        mid = left+(right-left)//2

        cur = weights[mid]

        if(dfs(a,b,cur)):
            answer = mid
            left=mid+1

        else:
            right = mid-1

        

    print(weights[answer])



if __name__=="__main__":
    solve()