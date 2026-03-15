import sys

input = sys.stdin.readline

def solve():
    r, c, k = map(int, input().split())
    
    maps = [list(input().strip()) for i in range(r)]
    visited = [[False] *c for _ in range(r)] 
    answer = 0
    

    def dfs(row, col, distance):
        nonlocal answer
        dr = [1, -1, 0, 0]
        dc = [0, 0, -1, 1]

        if row == 0 and col == c-1 and distance ==k:
            answer += 1
            return
        
        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]

            if (0<=nr<r and 0<=nc<c and not visited[nr][nc] and maps[nr][nc]!="T"):
                visited[nr][nc] = True
                dfs(nr,nc,distance+1)
                visited[nr][nc] = False

    visited[r-1][0] =True
    dfs(r-1,0,1)
    print(answer)
    

if __name__=="__main__":
    solve()