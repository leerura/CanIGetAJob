import sys

input = sys.stdin.readline

def solve():
    n,m = map(int, input().split()) #n이 row, m이 col
    maps = [list(map(int,input().split())) for _ in range(n)]   

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def dfs(start_row, start_col):
        maps[start_row][start_col] = 0

        area = 1

        for i in range(4):
            nr = start_row + dr[i]
            nc = start_col + dc[i]

            if(0<=nr<n and 0<=nc<m and maps[nr][nc]==1):
                area += dfs(nr,nc)
        return area

    count = 0
    max_result = 0
    for i in range(n):
        for j in range(m):
            if(maps[i][j]==1):
                count+=1
                result = dfs(i,j)
                max_result = max(max_result, result)

    print(count)
    print(max_result)


if __name__=="__main__":
    solve()

