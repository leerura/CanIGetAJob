import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def solve():
    n = int(input().strip())

    maps = [list(map(int,input().split())) for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_height = 0
    for row in range(n):
        for col in range(n):
            max_height = max(maps[row][col], max_height)

    max_count = 1

    for height in range(max_height):
        visited = [[False] * n for _ in range(n)]

        count = 0

        for row in range(n):
            for col in range(n):


                if(maps[row][col] <= height):
                    visited[row][col] = True

                    

        def dfs(start_row, start_col):
            nonlocal visited
            visited[start_row][start_col] = True

            area = 1

            for i in range(4):
                nr = start_row+dr[i]
                nc = start_col+dc[i]

                if(0<= nr < n and 0<= nc < n and not visited[nr][nc] == True):
                    visited[nr][nc] = True
                    dfs(nr,nc)

        
        for row in range(n):
            for col in range(n):
                if(visited[row][col] == False):
                    count +=1
                    dfs(row,col)
        max_count = max(max_count, count)
    print(max_count)
                    

if __name__=="__main__":
    solve()