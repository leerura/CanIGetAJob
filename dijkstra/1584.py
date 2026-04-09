import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    danger_zone = []
    for _ in range(n):
        x1,y1,x2,y2 = map(int,input().split())
        danger_zone.append((x1,y1,x2,y2))

    

    m = int(input().strip())
    death_zone= []
    for _ in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        death_zone.append((x1,y1,x2,y2))

    used_hp = [[float('inf') ] * 501 for _ in range(501)] #너무 큰 거 아닐까 hp[x][y] => x,y까지 가기 위해 사용해야하는 최소한의 hp

    def dijkstra(start_x, start_y):
        nonlocal used_hp

        dx = [0,0,-1,1]
        dy = [1,-1,0,0]

        q = []
        used_hp[start_x][start_y] = 0
        heapq.heappush(q,(0,start_x,start_y))

        while q:
            cur_cost, cur_x, cur_y = heapq.heappop(q)

            if(used_hp[cur_x][cur_y]<cur_cost):
                continue

            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if(0<= nx<501 and 0<=ny<501):
                    is_death = False #0이면 안전지역 1이면 위험지역 2면 죽음
                    is_danger = False
                    
                    #불필요함
                    for x1,y1,x2,y2 in death_zone:
                        if(min(x1,x2)<=nx<=max(x1,x2) and min(y1,y2)<=ny<=max(y1,y2)):
                            is_death = True
                            break
                    #불필요함
                    for x1,y1,x2,y2 in danger_zone:
                        if(min(x1,x2)<=nx<=max(x1,x2) and min(y1,y2)<=ny<=max(y1,y2)):
                            is_danger = True
                            break

                    #죽음 지역이라면
                    if(is_death):
                        continue
                    #위험 지역이라면
                    if(not is_death and is_danger):
                        if(used_hp[nx][ny]>cur_cost+1):
                            used_hp[nx][ny] = cur_cost+1
                            heapq.heappush(q,(used_hp[nx][ny],nx,ny))
                    #안전지역이라면
                    if(not is_death and not is_danger):
                        if(used_hp[nx][ny]>cur_cost):
                            used_hp[nx][ny] = cur_cost
                            heapq.heappush(q,(used_hp[nx][ny],nx,ny))


    dijkstra(0,0)

    print(used_hp[500][500] if used_hp[500][500] != float('inf') else -1)



    used_hp = [[float('inf') ] * 501 for _ in range(501)] #너무 큰 거 아닐까
    



if __name__=="__main__":
    solve()