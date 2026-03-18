import sys
from collections import deque

input = sys.stdin.readline

def solve():
    t = int(input().strip())

    for _ in range(t):
        answer = 0
        m, n, k = map(int, input().split())
        maps = [[0] *m for _ in range(n)]
        
        for __ in range(k):
            col, row = map(int, input().split())
            maps[row][col] = 1

        def bfs(row, col):
            dr = [-1,1,0,0]
            dc = [0,0,-1,1]
            nonlocal maps

            q = deque()
            maps[row][col] == 0
            q.append((row,col))

            while(q):
                cur_row, cur_col= q.popleft()

                for i in range(4):
                    nr = cur_row + dr[i]
                    nc = cur_col + dc[i]
                    if(0<=nr<n and 0<=nc<m and maps[nr][nc] == 1):
                        maps[nr][nc] = 0
                        q.append((nr,nc))
            return

        for j in range(n):
            for k in range(m):
                if(maps[j][k] == 1):
                    answer += 1
                    bfs(j,k)
        print(answer)



if __name__ == "__main__":
    solve()