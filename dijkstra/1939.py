import sys
import heapq

input = sys.stdin.readline

def solve():
    n,m = map(int,input().split()) #n: 섬개수, m: 다리 개수

    adj = [[] for _ in range(n+1)]

    for _ in range(m):
        u,v,w = map(int, input().split())

        adj[u].append((v,w))
        adj[v].append((u,w))

    a,b = map(int, input().split())

    def dijkstra(start):
        weight = [0] * (n+1) #무거울 수록 좋음 weight[i] i번째까지 갈 수 있는 최고...
        weight[start] = float('inf')


        q = []
        heapq.heappush(q, (-float('inf'), start))

        while(q):
            cur_weight, cur = heapq.heappop(q)
            cur_weight = -cur_weight


            #이건쫌 생각해봅시다
            if(weight[cur]>cur_weight):
                continue

            for next,w in adj[cur]:
                path_limit = min(cur_weight,w)

                if(weight[next]< path_limit):
                    weight[next] = path_limit
                    heapq.heappush(q, (-weight[next], next))

        return weight
    
    print(dijkstra(a)[b])

if __name__=="__main__":
    solve()