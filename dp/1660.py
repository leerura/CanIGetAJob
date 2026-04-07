import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    triangles = []

    number = 1

    while((number)*(number+1)*(number+2)//6<=n):
        triangles.append((number)*(number+1)*(number+2)//6)
        number+=1
    """
    dp = [float('inf')] * (n+1) #dp[i] = i개로 만들 수 있는 최소 개수
    dp[0] = 0

    

    for i in range(n+1):
        for triangle in triangles:
            if i-triangle>=0:
                dp[i] = min(dp[i],dp[i-triangle]+1)

    print(dp[n])
    """
    q = deque()
    visited = set()

    for triangle in triangles:
        if n==triangle:
            print(1)
            return
        q.append((triangle,1)) #한번으로 갈 수 있는 곳
        visited.add(triangle)

    while(q):
        cur, count = q.popleft()

        for triangle in triangles:
            if cur+triangle == n:
                print(count+1)
                return
            
            if(not cur+triangle in visited):
                visited.add(cur+triangle)
                q.append((cur+triangle,count+1))
    



if __name__=="__main__":
    solve()