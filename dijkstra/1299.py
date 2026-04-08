import sys
import heapq



input = sys.stdin.readline

def solve():
    n = int(input().strip())
    m = int(input().strip())

    dist = [float('inf')] * (n+1)
    
    adj = [[] for _ in range(n+1)]


    for _ in range(m):
        start, end, cost = map(int, input().split())
        adj[start].append((end, cost))

    start_node, end_node = map(int, input().split())

    def dijkstra(s):
        nonlocal dist
        q = []
        heapq.heappush(q,(0,s))
        dist[s] = 0

        while q:
            distance , cur = heapq.heappop(q)

            if (dist[cur]<distance): #이미 이 점은 최적화됨
                continue

            for next, cost in adj[cur]:
                if(dist[next]> distance+cost):
                    dist[next] = distance+cost
                    heapq.heappush(q,(dist[next],next))

    dijkstra(start_node)


    print(dist[end_node])


if __name__=="__main__":
    solve()

