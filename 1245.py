import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n,m = map(int,input().split()) #n이 row, m이 col

    heights =  [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    #상하좌우 오른쪽위 왼쪽위 왼쪽아래 오른쪽아래
    dr = [-1, 1, 0, 0 ,-1, -1, 1, 1]
    dc = [0, 0 , -1 , 1, 1, -1 ,-1 ,1]

    def bfs(r,c):
        nonlocal visited
        visited[r][c] = True
        target_height = heights[r][c]
        is_peak_flag = True

        q = deque()
        q.append((r,c))

        while(q):
            row, col = q.popleft()

            for i in range(8):
                nr = row + dr[i]
                nc = col + dc[i]
                if (0<=nr<n and 0<=nc<m):
                    if(heights[nr][nc] > target_height):
                        is_peak_flag = False

                    elif not visited[nr][nc] and heights[nr][nc] == target_height:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        return is_peak_flag
                


        

    answer = 0
    
    for row in range(n):
        for col in range(m):
            if(not visited[row][col] and bfs(row,col)):
                
                answer+=1
                

    print(answer)
            
            
    

if __name__ == "__main__":
    solve()