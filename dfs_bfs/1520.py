import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def solve():
    m, n = map(int, input().split()) #n = col, m = row

    heights = [list(map(int,input().split())) for _ in range(m)]
    memo = [[-1] *n for _ in range(m)]

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    def dfs(row, col):

        nonlocal memo
        if(row == m-1 and col == n-1):
            memo[row][col] = 1
            return memo[row][col]
        
        if(memo[row][col] != -1):
            return memo[row][col]
        
        memo[row][col] = 0
        
        for i in range(4):
            nr ,nc = row+dr[i],col+dc[i]

            if(0<=nr<m and 0<=nc<n and heights[nr][nc] < heights[row][col]):
                memo[row][col] += dfs(nr,nc)

        return memo[row][col]
        


    dfs(0, 0)

    print(memo[0][0])

if __name__=="__main__":
    solve()