import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m = map(int,input().split())

    adj = [[] for _ in range(n+1)]

    answer = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        u,v,w = map(int, input().split())

        adj[u].append((v,w))
        adj[v].append((u,w))


    def dijkstra(start):
        parent = [-1] *(n+1)
        dist = [float('inf')] *(n+1)

        dist[start] = 0
        q = []
        heapq.heappush(q,(0,start))


        #얘가 병목이 될 수도 있겠구나
        while(q):
            distance, cur = heapq.heappop(q)

            if(dist[cur]<distance):
                continue

            for next, weight in adj[cur]:
                if(dist[next]> distance+weight):
                    dist[next] = distance+weight
                    heapq.heappush(q,(dist[next],next))
                    parent[next] = cur
                    

        return parent
    

    for i in range(1,n+1):
        res = dijkstra(i)
        for j in range(1,n+1):
            if(i==j):
                answer[i][j] = "-"
            else:
                cur =j
                while(res[cur] !=i):
                    cur = res[cur]
                answer[i][j] = cur

    for i in range(1,n+1):
        row = answer[i]
        for j in range(1,n+1):
            print(row[j], end=" ")
        print()
        
    



if __name__=="__main__":
    solve()