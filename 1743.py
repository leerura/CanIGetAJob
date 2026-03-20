import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split()) #n이 row, m이 col

    maps = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        r,c = map(int,input().split())
        row = r-1
        col = c-1

        maps[row][col] = 1
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(row, col):
        count = 1
        maps[row][col] = 0
        q = deque()
        q.append((row, col))

        while(q):
            cur_row, cur_col = q.popleft()

            for i in range(4):
                nr = cur_row + dr[i]
                nc = cur_col + dc[i]
                if(0<=nr<n and 0<=nc<m and maps[nr][nc]==1):
                    maps[nr][nc]=0
                    q.append((nr,nc))
                    count += 1

        return count

    
    max_count = 0
    for i in range(n):
        for j in range(m):
            if(maps[i][j] == 1):
                count = bfs(i,j)
                max_count = max(count, max_count)

    print(max_count)

if __name__=="__main__":
    solve()