import sys
import heapq

input = sys.stdin.readline

def solve():
    n,m,x = map(int, input().split())


    adj = [[] for _ in range(n+1)]
    rev_adj = [[] for _ in range(n+1)]
    times = [0] *(n+1)

    for _ in range(m):
        u,v,w = map(int,input().split())
        adj[u].append((v,w))

        rev_adj[v].append((u,w))


    def dijkstra(adj_list, start):
        dist = [float('inf')] *(n+1)
        dist[start] = 0
        
        q=[]
        heapq.heappush(q,(0,start))

        while(q):
            distance, cur = heapq.heappop(q)

            if(dist[cur]<distance):
                continue

            for next, cost in adj_list[cur]:
                if(dist[next] > distance+cost):
                    dist[next] = distance+cost
                    heapq.heappush(q,(dist[next],next))

        return dist
    
    #돌아가는 거 먼저
    res1 = dijkstra(adj, x)

    for i in range(1,n+1):
        times[i] += res1[i]
    

    #오늘 걸 해야하는데....
    res2 = dijkstra(rev_adj,x)
    for i in range(1,n+1):
        times[i] += res2[i]

    max_value = 0

    for i in range(1,n+1):
        max_value = max(max_value, times[i])

    print(max_value)



if __name__=="__main__":
    solve()