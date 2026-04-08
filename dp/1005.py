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

        needed = set()
        
        degrees = [0]*(n+1)


        for _k in range(k):
            a,b = map(int,input().split())
            adj[a].append(b)
            degrees[b] = degrees[b]+1

            rev_adj[a].append(b)
            rev_adj[b].append(a)

        w = int(input().strip()) #w와 관련된 친구를 뽑아야함
        

        q1 = deque()
        needed = set()


        q1.append(w)
        needed.add(w)

        while(q1):
            cur = q1.popleft()

            for next in rev_adj[cur]:
                if(not next in needed):
                    needed.add(next)
                    q1.append(next)

        
    
        q = deque()

        for i in range(1,n+1):
            if(degrees[i]==0 and i in needed):
                q.append((i,1))

       
        data = {}
        created_at = 0
        cost = 0

 

        while(q):
            cur, count = q.popleft()
            if(cur==w):
                created_at = count
                cost = times[cur-1]

            time = times[cur-1]

            data[count] = max(time, data.get(count,0))

            for next in adj[cur]:
                degrees[next] = degrees[next]-1
                if(degrees[next]==0):
                    q.append((next,count+1))


        answer = 0

        for i in range(1,created_at):
            answer += data[i]

        answer += cost

        print(answer)
        
if __name__=="__main__":
    solve()