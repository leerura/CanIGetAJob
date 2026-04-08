import sys
from collections import deque

input = sys.stdin.readline

def solve():
    t = int(input().strip())

    for _ in range(t):
        n,k =map(int, input().split()) #n이 건물 개수 , k는 규칙개수

        times = list(map(int, input().split()))

        adj = [[] for _ in range(n+1)]
        rev_adj = [[] for _ in range(n+1)]

        
        degrees = [0]*(n+1)

        dp = [0] * (n+1) #dp[i] = i의 이전까지 다 끝내는데 걸리는 시간 => dp[i] = max(dp[precessor]+times[precessor-1])


        for _k in range(k):
            a,b = map(int,input().split())
            adj[a].append(b)
            degrees[b] = degrees[b]+1

            rev_adj[b].append(a)

        q = deque()

        for i in range(1,n+1):
            if(degrees[i]==0):
                q.append(i)

        w = int(input().strip()) 

        while(q):
            cur = q.popleft()

            for precessor in rev_adj[cur]:
                dp[cur] = max(dp[precessor]+times[precessor-1],dp[cur])

            for next in adj[cur]:
                degrees[next] = degrees[next]-1
                if degrees[next] == 0:
                    q.append(next)


        print(dp[w]+times[w-1])
        

        
    
        
        
if __name__=="__main__":
    solve()