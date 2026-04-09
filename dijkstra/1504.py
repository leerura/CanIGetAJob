import sys
import heapq

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b,e = map(int,input().split())
        adj[a].append((b,e))
        adj[b].append((a,e))

    c1, c2 = map(int, input().split())

    def dijkstra(start):
        dist = [float('inf')]*(n+1)
        q=[]
        heapq.heappush(q, (0,start))
        dist[start] = 0

        while(q):
            distance, cur = heapq.heappop(q)

            if(dist[cur]<distance):
                continue

            for next, cost in adj[cur]:
                if(dist[next]> distance + cost):
                    dist[next] = distance + cost
                    heapq.heappush(q, (dist[next],next) )

        return dist
    
    first = dijkstra(1)

    if(first[c1]+first[c2]+first[n] == float('inf')):
        print(-1)
        return
    
    
    print(min(first[c1]+dijkstra(c1)[c2]+dijkstra(c2)[n],first[c2]+dijkstra(c2)[c1]+dijkstra(c1)[n]))
    

if __name__=="__main__":
    solve()