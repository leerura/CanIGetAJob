import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    b_answer = 0
    w_answer = 0
    maps = [input().strip() for _ in range(m)]

    num_maps = [[0] * n for _ in range(m)]

    
    
    for i in range(m):
        for j in range(n):
            if(maps[i][j] == "B"):
                num_maps[i][j] = 1
            else:
                num_maps[i][j] = 2

     
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(row, col, color):
        nonlocal maps
        
        num_maps[row][col] = 0
        size = 1

        q = deque()
        q.append((row,col))

        while(q):
            cur_row, cur_col = q.popleft()
            for i in range(4):
                nr = cur_row + dr[i]
                nc = cur_col + dc[i]

                if(0<= nr < m and 0 <= nc < n and num_maps[nr][nc] == color):
                    num_maps[nr][nc] = 0
                    size +=1
                    q.append((nr,nc))
        return size

    for i in range(m):
        for j in range(n):
            if(num_maps[i][j] == 1):
                size = bfs(i,j, 1)
                b_answer += size**2

    for i in range(m):
        for j in range(n):
            if(num_maps[i][j] == 2):
                size = bfs(i,j, 2)
                w_answer += size**2

    print(w_answer, b_answer)

if __name__ =="__main__":
    solve()