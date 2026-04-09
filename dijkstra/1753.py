import sys

input = sys.stdin.readline

def solve():
    v,e = map(int,input().split())

    k = int(input().strip())

    #여러 개의 간선이 존재할 수 있음
    adj = [[] for _ in range(v+1)]
    dist = [float('inf')] *(v+1)

    for _ in range(e):
        start,end,w = map(int, input().split())

        adj[start].append((end,w))

    def dijkstra(start_node):
        dist[start_node] = 0

        


    dijkstra(0)

    for i in range(1,v+1):
        print(dist[i] if dist[i] != float("inf") else "INF")



if __name__=="__main__":
    solve()