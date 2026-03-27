import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    queens = list(map(int,input().split()))
    knights = list(map(int,input().split()))
    pawns = list(map(int,input().split()))

    visited = [[0]*m for _ in range(n)] #0: 방문 안함, 1: 방문함. 2: 장애물이 있는

    num_pawns = pawns[0]

    for i in range(num_pawns):
        row,col = pawns[2*i+1]-1, pawns[2*i+2]-1
        visited[row][col] = 2

    knight_moves = {(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)}

    num_knights = knights[0]
    for i in range(num_knights):
        row,col = knights[2*i+1]-1, knights[2*i+2]-1
        visited[row][col] = 2

        for dr, dc in knight_moves:
            nr = row+dr
            nc = col+dc
            if(0<=nr<n and 0<=nc<m and visited[nr][nc]!=2):
                visited[nr][nc] = 1

    num_queens = queens[0]

    queen_moves = {(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)}

    for i in range(num_queens):
        row,col = queens[2*i+1]-1, queens[2*i+2]-1
        visited[row][col] = 2

    for i in range(num_queens):
        row,col = queens[2*i+1]-1, queens[2*i+2]-1
        for dr,dc in queen_moves:
            nr,nc = row+dr,col+dc
            while(0<=nr<n and 0<=nc<m and visited[nr][nc]!=2):
                visited[nr][nc] = 1
                nr, nc =nr+dr,nc+dc
            

    answer = 0
    for row in range(n):
        for col in range(m):
            if(visited[row][col]==0):
                answer += 1
        
    print(answer)


if __name__ =="__main__":
    solve()