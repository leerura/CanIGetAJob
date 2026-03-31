import sys
from collections import deque

def solve():

    maps = {}

    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 3:
            continue
        v1,v2,edge = map(int,parts)

        maps.setdefault(v1,[]).append((v2,edge))
        maps.setdefault(v2,[]).append((v1,edge))

    
    def bfs(start_vertex):
        dist = {node: -1 for node in maps.keys()}
        

        dist[start_vertex] = 0

        q = deque()

        q.append(start_vertex)

        
        while(q):
            cur = q.popleft()

            for next, edge in maps.get(cur,[]):
                if(dist[next] == -1):
                    dist[next] = dist[cur] + edge
                    q.append(next)

        max_distance = 0
        max_vertex = 0

        for key in maps.keys():
            if(dist[key]>max_distance):
                max_distance = dist[key]
                max_vertex = key

        return max_vertex, max_distance
    
    v1, _ = bfs(1)
    v2, answer = bfs(v1)

    print(answer)
    
if __name__=="__main__":
    solve()