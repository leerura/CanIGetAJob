import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # n<=백만... 무조건 O(n)에 마무리...
    n,m = map(int,input().split())

    maps = {}

    maps.setdefault("alice", []).append("hi")
   

    
    for _ in range(m):
        a,b = input().split()
        maps.setdefault(a, []).append(b)
        #adj[a].append(b)

    def bfs(start, end):

        visited = set()
        visited.add(start)

        q = deque()
        q.append(start)

        while(q):
            cur = q.popleft()

            for next in maps.get(cur,[]):
                if(next == end):
                    return True
                if(not next in visited):
                    visited.add(next)
                    q.append(next)

        return False
    
    quries = int(input().strip())


    #할 때마다 bfs를 실행하는 것이 병목...
    for _ in range(quries):
        a,b = input().split()

        res_ab = bfs(a, b)
        res_ba = bfs(b, a)

        if not res_ab and not res_ba: print("gg", end=" ")
        elif res_ab: print(a, end=" ")
        else: print(b, end=" ")

if __name__ == "__main__":
    solve()

