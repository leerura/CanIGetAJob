import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    maps = [list(input().strip()) for _ in range(n)]

    
    def dijkstra(start_row, start_col):
        cost = [[float("inf")]*n for _ in range(n)] #cost[row][col] (row,col)에 도달하기 위해 꺠어야하는 흑돌의 최소개수

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        cost[start_row][start_col] = 0

        q=[]
        heapq.heappush(q,(0,start_row,start_col))

        while(q):
            cur_cost, cur_row,cur_col = heapq.heappop(q)

            if(cost[cur_row][cur_col]<cur_cost): 
                continue

            for i in range(4):
                nr = cur_row+dr[i]
                nc = cur_col+dc[i]

                if(0<=nr<n and 0<=nc<n):
                    #흰돌인 경우
                    if(int(maps[nr][nc])==1 and cost[nr][nc]>cur_cost):
                        cost[nr][nc] = cur_cost
                        heapq.heappush(q,(cost[nr][nc],nr,nc))
                    #흑돌인 경우
                    elif(int(maps[nr][nc])==0 and cost[nr][nc]>cur_cost+1):
                        cost[nr][nc]=cur_cost+1
                        heapq.heappush(q,(cost[nr][nc],nr,nc))


        return cost[n-1][n-1]
    
    print(dijkstra(0,0))
    
if __name__=="__main__":
    solve()