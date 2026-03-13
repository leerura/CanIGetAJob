import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split()) #n이 세로(행) m이 가로(열)

    boards = [list(input().strip()) for _ in range(n)]
    
    
    error_grid = [[0 for _ in range(m) ] for _ in range(n)]

    

    
    for i in range(n):
        for j in range(m):
            if((i+j)%2 ==0 and boards[i][j] == 'B') or ((i+j)%2 ==1 and boards[i][j] == 'W'):
                error_grid[i][j] = 1
                

    s  = [[0 for _ in range(m+1) ] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = error_grid[i-1][j-1] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]

    min_count = float('inf')

    for i in range(8,n+1):
        for j in range(8,m+1):
            cnt = s[i][j] - s[i-8][j] - s[i][j-8] + s[i-8][j-8]
            min_count = min(min_count, cnt, 64-cnt)
    print(min_count)
            

if __name__ == "__main__":
    solve()