import sys
import heapq

input = sys.stdin.readline

def solve():
    m,n = map(int,input().split()) #m이 col n이 row
    
    maps =[input().strip() for _ in range(n)]

    dist = [[float('inf')]  * m for _ in range(n)] #like dp dist[row][col] = 그곳으로 가기위해 부셔야할 벽의 최소 개수
    
    def dijkstra(start_row, start_col):
        dist[start_row][start_col] = 0
        q=[]
        heapq.heappush(q,(0,start_row,start_col))

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        while(q):
            cost , cur_row, cur_col = heapq.heappop(q)

            if(dist[cur_row][cur_col]<cost):
                continue

            for i in range(4):
                nr = cur_row +dr[i]
                nc = cur_col +dc[i]
                if(0<=nr<n and 0<=nc<m and dist[nr][nc] > cost + int(maps[nr][nc])):
                    dist[nr][nc] = cost + int(maps[nr][nc])
                    heapq.heappush(q,(dist[nr][nc],nr,nc))

    
    dijkstra(0,0)
    print(dist[n-1][m-1])

    

if __name__=="__main__":
    solve()